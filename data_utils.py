import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

class Dataset():
    def __init__(self, path, shuffle):
        self._data = pd.read_csv(path)
        self._label_column = self._data.columns[-1]
        
        if shuffle:
            self._shuffle_data()

    def _shuffle_data(self):
        self._data = self._data.sample(frac=1).reset_index(drop=True)

    def __len__(self):
        return len(self._data)

    def get_data(self, normalize = True):
        labels = self._data[self._label_column]
        features = self._data.drop(self._label_column, 1)

        if normalize:
            scaler = StandardScaler()
            scaler.fit(features)
            features = pd.DataFrame(scaler.transform(features))

        return features, labels

    def __getitem__(self, idx):
        features = self._data.iloc[idx].drop(self._label_column)
        features = features.to_frame().transpose()

        label = self._data.iloc[idx][self._label_column]

        return features, label


class Ecoli(Dataset):
    def __init__(self, path='datasets/ecoli/ecoli.csv', shuffle=True):
        super().__init__(path, shuffle)


class Glass(Dataset):
    def __init__(self, path='datasets/glass/glass.csv', shuffle=True):
        super().__init__(path, shuffle)


class Haberman(Dataset):
    def __init__(self, path='datasets/haberman/haberman.csv', shuffle=True):
        super().__init__(path, shuffle)


class Ionosphere(Dataset):
    def __init__(self, path='datasets/ionosphere/ionosphere.csv', shuffle=True):
        super().__init__(path, shuffle)


class Iris(Dataset):
    def __init__(self, path='datasets/iris/iris.csv', shuffle=True):
        super().__init__(path, shuffle)


class Pima(Dataset):
    def __init__(self, path='datasets/pima/diabetes.csv', shuffle=True):
        super().__init__(path, shuffle)


class Sonar(Dataset):
    def __init__(self, path='datasets/sonar/sonar.csv', shuffle=True):
        super().__init__(path, shuffle)

class Thyroid(Dataset):
    def __init__(self, path='datasets/thyroid/thyroid.csv', shuffle=True):
        super().__init__(path, shuffle)
        self._label_column = self._data.columns[0]


class Vehicle(Dataset):
    def __init__(self, path='datasets/vehicle/vehicle.csv', shuffle=True):
        super().__init__(path, shuffle)


class WDBC(Dataset):
    def __init__(self, path='datasets/wdbc/wdbc.csv', shuffle=True):
        super().__init__(path, shuffle)
        self._label_column = self._data.columns[1]


class Wine(Dataset):
    def __init__(self, path='datasets/wine/wine.csv', shuffle=True):
        super().__init__(path, shuffle)
        self._label_column = self._data.columns[0]


def get_all_datasets():
    datasets = {'Ecoli': Ecoli(),
                'Glass': Glass(),
                'Haberman': Haberman(),
                'Ionosphere': Ionosphere(),
                'Iris': Iris(),
                'Pima': Pima(),
                'Sonar': Sonar(),
                'Thyroid': Thyroid(),
                'Vehicle': Vehicle(),
                'WDBC': WDBC(),
                'Wine': Wine()}

    return datasets
