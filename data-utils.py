import pandas as pd


class Ecoli():
    def __init__(self, path='datasets/ecoli/ecoli.data', shuffle=True):
        self.__columns = ['Sequence Name', 'mcg', 'gvh', 'lip', 'chg', 'aac',
                          'alm1', 'alm2', 'class']
        self.__label_column = 'class'
        self._data = pd.read_csv(path, names=self.__columns)

        if shuffle:
            self._data = self._data.sample(frac=1).reset_index(drop=True)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, idx):
        features = self._data.iloc[idx].drop(self.__label_column)
        features = features.to_frame().transpose()

        label = self._data.iloc[idx][self.__label_column]

        return features, label
