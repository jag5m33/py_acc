import xgboost as xgb
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, average_precision_score, precision_recall_curve)
import matplotlib.pyplot as plt


class Xgboost:
    def __init__(self, x_train, y_train, x_val, y_val, x_test, y_test):
        self.x_train = x_train
        self.y_train = y_train
        self.x_val = x_val
        self.y_val = y_val
        self.x_test = x_test
        self.y_test = y_test

        self.model = xgb.XGBClassifier(objective = 'binary:logistic',
                                  random_state = 42)
    def train(self):
        print("training model for binary classification")
        self.model.fit(self.x_train, y_train)
        print(f" number of trees across full model: {len(self.model.get_booster().get_dump())}")

    def _score(self, x, y, name):
        preds = self.model.predict(x)
        #probability it is severe: class 1
        probs = self.model.predict_proba(x)[:, 1] # P(severe) for each row; column 1 = class 1 (column 0: class 0: probability, column 1: class 1: probability)

        scores = {
            "accuracy": accuracy_score(y, preds),
            "precision": precision_score(y, preds, zero_division=0),
            "recall": recall_score(y, preds),
            "f1": f1_score(y, preds),
            "pr_auc": average_precision_score(y, probs),
            "pred_rate": preds.mean(), # this tells us if there were more 1 or 0 prediceted (mean is easily skewed)
            "true_rate": y.mean() # what is the mean of the actual values (same as predicted or no) - if similar or same = shows that they are predicting semi-correct
        }

        #name - train, test, val etc.
        print(f"{name:<10} acc {scores['accuracy']:.4f} | "
              f"prec {scores['precision']:.4f} | rec {scores['recall']:.4f} | "
              f"F1 {scores['f1']:.4f} | PR-AUC {scores['pr_auc']:.4f} | "
              f"predicted severe {scores['pred_rate']:.3f} vs actual {scores['true_rate']:.3f}")

        return preds, probs, scores 
    
    def evaluate_train(self):
        return self._score(self.x_train, self.y_train, 'Train')

    def validate(self):
        return self._score(self.x_val, self.y_val, 'Validation')
    def eval_test(self):
        return self._score(self.x_test, self.y_test, 'Test')

    def plot_pr_curve(self, x, y, name = 'validation'):
        probs = self.model.predict_proba(x)[:, 1] # get the severity 
        precision, recall, thresholds = precision_recall_curve(y, probs)
        plt.figure(figsize=(7, 5))
        plt.plot(recall, precision, label=f'AP = {average_precision_score(y, probs):.3f}')
        plt.axhline(y.mean(), color='red', linestyle='--',
                    label=f'baseline {y.mean():.3f}')                      # what random guessing would score
        plt.xlabel('recall')
        plt.ylabel('precision')
        plt.title(f'Precision-recall curve - {name}')
        plt.legend()
        plt.grid(alpha=0.3)
        plt.show()

        return precision, recall, thresholds # # thresholds lets you pick an operating point other than 0.5
    