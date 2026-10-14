import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

## ERROR ANALYSIS VIA FEATURES AND THEIR IMPORTANCE TOO 

class ErrorAnalysis:
    # Study one model's mistakes on ONE split (normally validation).
    # y_true : the real labels, 0 = not severe, 1 = severe
    # y_pred : the model's guesses at the 0.5 threshold
    # probs  : P(severe) for each row, from predict_proba[:, 1]
    # x      : the feature frame for this split, so errors can be broken down by column
    def __init__(self, y_true, y_pred, probs, x):
        self.y_true = np.asarray(y_true)
        self.y_pred = np.asarray(y_pred)
        self.probs = np.asarray(probs)
        self.x = x

    # 1. THE FOUR CELLS: TP / FP / FN / TN as plain counts
    def counts(self):
        tn, fp, fn, tp = confusion_matrix(self.y_true, self.y_pred).ravel()
        return pd.Series({
            "TP": tp,    # correctly called severe
            "FP": fp,    # called severe, wasn't          -> false alarm
            "FN": fn,    # was severe, called not severe  -> missed
            "TN": tn,    # correctly called not severe
        })

    # 2. PER-CLASS SCORES: precision, recall, F1 for both classes
    def report_df(self):
        report = classification_report(self.y_true, self.y_pred,
                                       target_names=["not severe", "severe"],
                                       output_dict=True, zero_division=0)
        return pd.DataFrame(report).T.round(4)

    # 3. WHERE THE ERRORS LIVE: error rate broken down by one feature
    #    This is the real error analysis - which road types, hours or states
    #    does the model get wrong? Compare against the overall error rate.
    def errors_by(self, column, min_rows=500):
        wrong = self.y_true != self.y_pred
        table = pd.DataFrame({
            column: self.x[column].values,
            "wrong": wrong,
            "missed": (self.y_true == 1) & (self.y_pred == 0),      # FN
            "false_alarm": (self.y_true == 0) & (self.y_pred == 1), # FP
        })
        out = table.groupby(column).agg(
            rows=("wrong", "size"),
            error_rate=("wrong", "mean"),
            missed_rate=("missed", "mean"),
            false_alarm_rate=("false_alarm", "mean"),
        ).round(4)
        out = out[out.rows >= min_rows]                  # ignore groups too small to read
        return out.sort_values("error_rate", ascending=False)

    # 4. THE WORST MISTAKES: rows the model was most confident about and still got wrong
    #    High probability but actually not severe, or low probability but actually severe
    def worst_mistakes(self, n=20):
        df = self.x.copy()
        df["true"] = self.y_true
        df["prob_severe"] = self.probs
        df["error_size"] = (self.y_true - self.probs).abs()   # how far off the model was
        return df[self.y_true != self.y_pred].sort_values("error_size", ascending=False).head(n)

    # 5. CONFUSION MATRIX PLOT: rows = true, columns = predicted
    #    normalize="true" -> each row shows shares, so the 66/34 imbalance doesn't hide the errors
    def plot_confusion_matrix(self):
        fig, ax = plt.subplots(figsize=(5, 4))
        ConfusionMatrixDisplay.from_predictions(
            self.y_true, self.y_pred, display_labels=["not severe", "severe"],
            normalize="true", ax=ax, cmap="Blues", colorbar=False)
        ax.set_title("Validation confusion matrix")
        plt.show()

    # 6. FEATURE IMPORTANCE: which columns the tree actually used
    #    Compare this against the Stage 2 ranking - does the model agree?
    def feature_importance(self, model, n=20):
        return (pd.Series(model.feature_importances_, index=self.x.columns)
                .sort_values(ascending=False).head(n).round(4))