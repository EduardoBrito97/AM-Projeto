import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from kss import KSS

def get_fitness(expression, dataset):
    kss_model = new KSS(7)
    kss_model.set_expression(expression)
    
    X_train,X_test,y_train,y_test = train_test_split(features.to_numpy(),labels.to_numpy(),test_size=0.2,random_state=4)

    kss_model.fit(X_train,y_train,'SEP')
    y_pred = kss_model.predict(X_test)

    report = metrics.classification_report(y_test, y_pred)

    return report['macro avg']['f1-score']