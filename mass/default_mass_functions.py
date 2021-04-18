import pandas as pd
from mass_entries import get_infos


class DefaultMass:
    def __init__(self, dataset_name, features, labels, x_q, class_q):
        self.dataset_name = dataset_name
        self.dataset = dataset = pd.concat([features.astype(float), labels], axis=1)
        self.instance = x_q
        self.label = class_q
        self.pcis = get_infos(self.dataset, self.instance, self.label)
    
    def ecoli(self):
        expr1 = (self.pcis["pc5"] + self.pcis["pc9"]) ** 0.5
        expr2 = 107.0172 * (expr1/self.pcis["pc4"])
        return 3.2749 - expr2

    def glass(self):
        expr1 = 6.0104 * (10 ** 15) * (self.pcis["pc9"] ** 0.5) * (self.pcis["pc3"] - self.pcis["pc7"])
        expr2 = (2.8823 * (10 ** 17) * self.pcis["pc6"]) + (5.3608 * (10 ** 17))
        return (expr1/expr2) + 3.7029

    def haberman(self):
        expr1 = 8.5856 * (10 ** (-7))
        expr2 = (self.pcis["pc7"] ** 2) / (self.pcis["pc6"] ** 2)
        return 1.13845 - (expr1 * expr2)

    def ionosphere(self):
        return (0.0115 * self.pcis["pc10"]) + 0.3545

    def iris(self):
        return (0.5095 * self.pcis["pc5"]) - (0.0089 * self.pcis["pc8"]) + 3.8569 + (0.0027 * self.pcis["pc1"]) + (0.0471  * self.pcis["pc6"] * self.pcis["pc9"])

    def pima(self):
        expr1 = 4.6357 * (10 ** (-8)) * (self.pcis["pc7"] ** 2) * self.pcis["pc9"]
        expr2 = 6.7395 * (10 ** (-8)) * (self.pcis["pc7"] ** 2)
        return expr1 + expr2 + 0.0014

    def sonar(self):
        return 1.4015 - (0.0269 * (self.pcis["pc8"] ** (1/2)))

    def thyroid(self):
        return 2.8450 - (0.0133 * self.pcis["pc2"])

    def vehicle(self):
        return 2.5963 - (0.1954 * self.pcis["pc10"])

    def wdbc(self):
        return 0.8835 - (0.0638 * self.pcis["pc5"])

    def wine(self):
        return (0.9508 * self.pcis["pc1"]) + 0.7208

    def assign_mass(self):
        if self.dataset_name == "ecoli":
            return self.ecoli()
        elif self.dataset_name == "glass":
            return self.glass()
        elif self.dataset_name == "haberman":
            return self.haberman()
        elif self.dataset_name == "ionosphere":
            return self.ionosphere()
        elif self.dataset_name == "iris":
            return self.iris()
        elif self.dataset_name == "pima":
            return self.pima()
        elif self.dataset_name == "sonar":
            return self.sonar()
        elif self.dataset_name == "thyroid":
            return self.thyroid()
        elif self.dataset_name == "vehicle":
            return self.vehicle()
        elif self.dataset_name == "wdbc":
            return self.wdbc()
        elif self.dataset_name == "wine":
            return self.wine()
        else:
            raise KeyError("Dataset not implemented")


if __name__ == "__main__":
    df = pd.read_csv("../datasets/iris/iris.csv",header=None)
    features, labels = df.iloc[1:, 0:-1].copy(), df.iloc[1:,-1].copy()

    mass = DefaultMass("iris", features, labels, [5.0,3.6,1.4,0.2], "Iris-setosa")
    print(mass.assign_mass())