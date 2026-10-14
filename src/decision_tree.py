from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, average_precision_score, precision_recall_curve)
import matplotlib.pyplot as plt


class BinaryDecisionTreeClassifier:
    def __init__(self, x_train, x_val, y_train, y_val, x_test, y_test, max_depth, min_samples_leaf, min_samples_split, max_features, class_weight = None):
        self.x_train = x_train
        self.y_train = y_train
        self.x_val = x_val
        self.y_val = y_val
        self.x_test = x_test
        self.y_test = y_test

        # model 

        self.model = DecisionTreeClassifier(max_depth = max_depth, # how many splits from root to leaf before making a decision; number of leaves double per level 
                                       min_samples_leaf= min_samples_leaf, # minimum samples per leaf; with a dataset of 2 million, 500 is adequate to make aconviced decision of equal disitribution
                                       #max_features = 'sqrt', # at each level; tree tests remaining features and picks the one with best information gain, so 31 sqrt = 6 - so test 6 of 31 per level
                                       min_samples_split  = min_samples_split,
                                       random_state= 42,
                                       max_features= max_features,
                                       class_weight= class_weight)
    def train(self):
        print("Training Decision tree for binary classification...")
        self.model.fit(self.x_train, self.y_train)
        print(f"Number of classes: {len(self.model.classes_)}")

    def _score(self, x, y, name):
        preds = self.model.predict(x)                  # hard 0/1 labels, thresholded at 0.5
        probs = self.model.predict_proba(x)[:, 1]      # P(severe) for each row; column 1 = class 1 (column 0: class 0: probability, column 1: class 1: probability)

        scores = {
            "accuracy":  accuracy_score(y, preds),                      # sanity reference only: predicting all-not-severe scores ~0.66
            "precision": precision_score(y, preds, zero_division=0),    # of those flagged severe, how many were right
            "recall":    recall_score(y, preds),                        # of the real severe accidents, how many were caught
            "f1":        f1_score(y, preds),                            # harmonic mean of the two, severe class only
            "pr_auc":    average_precision_score(y, probs),             # area under the PR curve: threshold-independent
            "pred_rate": preds.mean(),                                  # share the model called severe
            "true_rate": y.mean(),                                      # share actually severe; pred_rate far below this = model playing safe
        }

        print(f"{name:<10} acc {scores['accuracy']:.4f} | "
              f"prec {scores['precision']:.4f} | rec {scores['recall']:.4f} | "
              f"F1 {scores['f1']:.4f} | PR-AUC {scores['pr_auc']:.4f} | "
              f"predicted severe {scores['pred_rate']:.3f} vs actual {scores['true_rate']:.3f}")

        return preds, probs, scores

    def evaluate_train(self):
        return self._score(self.x_train, self.y_train, "train")

    def validate(self):
        return self._score(self.x_val, self.y_val, "validation")

    def eval_test(self):
        return self._score(self.x_test, self.y_test, "test")

    def plot_pr_curve(self, x, y, name="validation"):
        probs = self.model.predict_proba(x)[:, 1]
        precision, recall, thresholds = precision_recall_curve(y, probs)   # one point per distinct threshold

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

        return precision, recall, thresholds    # thresholds lets you pick an operating point other than 0.5