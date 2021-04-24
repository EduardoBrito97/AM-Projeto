import os
import glob
import pandas as pd

from kss import KSS
from data_utils import get_all_datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold

N_SPLITS = 10
RESULTS_PATH = './results'

def clean_logs(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    else:
        return

    logs = glob.glob(f'{path}/*')
    for log in logs:
        os.remove(log)


def main():
    clean_logs(RESULTS_PATH)

    datasets = get_all_datasets()
    algorithms = {'kNN': KNeighborsClassifier(n_neighbors=7),
                  'DWkNN': KNeighborsClassifier(n_neighbors=7, weights='distance'),
                  'DTree': DecisionTreeClassifier(max_depth=7),
                  'NBayes': GaussianNB(),
                  'SVM': SVC(C=8.5),
                  'MLP': MLPClassifier(hidden_layer_sizes=(12, 12, 12),
                                       max_iter=500)}

    df = pd.DataFrame(columns=['Dataset']+list(algorithms.keys()))

    for data_id, data in datasets.items():
        features, labels = data.get_data()

        aux_dict = {'Dataset': [data_id]}
        kf = KFold(n_splits=N_SPLITS, random_state=None, shuffle=True)
        kf.get_n_splits(features)

        for alg_id, alg in algorithms.items():
            f1_score = 0
            for train_idx, test_idx in kf.split(features):
                x_train, x_test = features.iloc[train_idx], features.iloc[test_idx]
                y_train, y_test = labels.iloc[train_idx], labels.iloc[test_idx]

                alg.fit(x_train, y_train)
                y_pred = alg.predict(x_test)

                f1_score += metrics.classification_report(y_test, y_pred,
                                                          output_dict=True,
                                                          zero_division=1)['macro avg']['f1-score']
            aux_dict[alg_id] = [f1_score/N_SPLITS]

        df = pd.concat([df, pd.DataFrame.from_dict(aux_dict)])

    df.loc['MEAN'] = df.mean()
    df.to_csv('all_algorithms.csv', index=False, float_format='%.4f') 

if __name__ == '__main__':
    main()
