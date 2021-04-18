from kss import KSS
from data_utils import Iris
from sklearn import metrics
from sklearn.model_selection import train_test_split

data = Iris()
features, labels = data.get_data()

print(features)
print('---------')
print(labels)

X_train,X_test,y_train,y_test = train_test_split(features.to_numpy(),labels.to_numpy(),test_size=0.2,random_state=4)

k_range = range(1,20)

for k in k_range:
  kss = KSS(k)
  kss.fit(X_train,y_train,'SEP')
  y_pred = kss.predict(X_test)

  print(k)

  print(metrics.classification_report(y_test, y_pred))