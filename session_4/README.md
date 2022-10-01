# Session 4

## Notes on Introduction to Evaluation Metrics

- Precision tells us what fraction of positive decision did we get right

- Accuracy tells us how many decisions(positive & negative) did we get right

- Recall, In simpler terms, of all the predictions that are correct how many of them are actually positive - either from the negative sample or positive sample

- Knowing metrics like precision, recall and auc is important for building great models to tackle the class imbalance problem when building binary classification model

- Get the `TPR`(True Postive Rate) to be as high as possible  for binary classification models and `FPR`(False Positive Rate) to be as low as possible.

- `AUC`(Area Under Curve) tells us how well our model is doing as it separates positive from negative classes. A great metric for binary classification.

- If you want know how stable your model is across different partitions in your dataset then use cross validation.

- AUC is one of the go-to great metric for evaluating binary classification models is because it tells us how well our model is doing when separating positive classes from negative ones.
