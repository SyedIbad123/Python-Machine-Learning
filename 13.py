import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split
import matplotlib as plt



# X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LogisticRegression()
# model.fit(X_train, y_train)
# y_pred_proba = model.predict_proba(X_test)
# fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:,1])

# plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1], linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('1 - specificity')
plt.ylabel('sensitivity')
plt.show()