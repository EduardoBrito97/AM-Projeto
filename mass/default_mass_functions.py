import pandas as pd
from mass_entries import get_infos


class DefaultMass:
    def __init__(self, dataset_name, features, labels):
        self.dataset_name = dataset_name
        self.features = features
        self.labels = labels
        self.mass = []

    def calculate_mass(self):
        for i in range(len(self.features)):
            self.pcis = get_infos(self.features, self.labels, self.features[i],self.labels[i])
            if self.dataset_name == "ecoli":
                self.mass.append(self.ecoli())
            elif self.dataset_name == "glass":
                self.mass.append(self.glass())
            elif self.dataset_name == "haberman":
                self.mass.append(self.haberman())
            elif self.dataset_name == "ionosphere":
                self.mass.append(self.ionosphere())
            elif self.dataset_name == "iris":
                self.mass.append(self.iris())
            elif self.dataset_name == "pima":
                self.mass.append(self.pima())
            elif self.dataset_name == "sonar":
                self.mass.append(self.sonar())
            elif self.dataset_name == "thyroid":
                self.mass.append(self.rhyroid())
            elif self.dataset_name == "vehicle":
                self.mass.append(self.vehicle())
            elif self.dataset_name == "wdbc":
                self.mass.append(self.wdbc())
            elif self.dataset_name == "wine":
                return self.mass.append(self.wine())
            else:
                raise KeyError("Dataset not implemented")
        return self.mass
    
    def ecoli(self):
        expr1 = (self.pcis["pc5"] + self.pcis["pc9"]) ** 0.5
        expr2 = 107.0172 * (expr1 / self.pcis["pc4"])

        mass = 3.2749 - expr2
        return mass

    def glass(self):
        expr1 = 6.0104 * (10 ** 15) * (self.pcis["pc9"] ** 0.5) * (self.pcis["pc3"] - self.pcis["pc7"])
        expr2 = (2.8823 * (10 ** 17) * self.pcis["pc6"]) + (5.3608 * (10 ** 17))

        mass =  (expr1/expr2) + 3.7029
        return mass

    def haberman(self):
        expr1 = 8.5856 * (10 ** (-7))
        expr2 = (self.pcis["pc7"] ** 2) / (self.pcis["pc6"] ** 2)

        mass = 1.13845 - (expr1 * expr2)
        return mass

    def ionosphere(self):
        mass =  (0.0115 * self.pcis["pc10"]) + 0.3545
        return mass

    def iris(self):
        mass = (0.5095 * self.pcis["pc5"]) - (0.0089 * self.pcis["pc8"]) + 3.8569 + (0.0027 * self.pcis["pc1"]) + (0.0471  * self.pcis["pc6"] * self.pcis["pc9"])
        return mass

    def pima(self):
        expr1 = 4.6357 * (10 ** (-8)) * (self.pcis["pc7"] ** 2) * self.pcis["pc9"]
        expr2 = 6.7395 * (10 ** (-8)) * (self.pcis["pc7"] ** 2)

        mass = expr1 + expr2 + 0.0014
        return mass

    def sonar(self):
        mass = 1.4015 - (0.0269 * (self.pcis["pc8"] ** (1/2)))
        return mass

    def thyroid(self):
        mass = 2.8450 - (0.0133 * self.pcis["pc2"])
        return mass

    def vehicle(self):
        mass = 2.5963 - (0.1954 * self.pcis["pc10"])
        return mass

    def wdbc(self):
        mass = 0.8835 - (0.0638 * self.pcis["pc5"])
        return mass

    def wine(self):
        mass = (0.9508 * self.pcis["pc1"]) + 0.7208
        return mass


if __name__ == "__main__":
    df = pd.read_csv("datasets/iris/iris.csv",header=None)
    features, labels = df.iloc[1:, 0:-1].to_numpy().astype(float), df.iloc[1:,-1].to_numpy()
    mass = DefaultMass("iris", features, labels)
    print(mass.calculate_mass())