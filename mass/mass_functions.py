import pandas as pd

def get_infos(dataset):
    n_classes = len(dataset[dataset.columns[-1]].unique())

# Test
df = pd.read_csv("datasets/iris/iris.data")
get_infos(df)