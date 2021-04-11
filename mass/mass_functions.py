from mass_entries import get_infos
import pandas as pd

# pc1 = 1
# pc2 = 1
# pc3 = 1
# pc4 = 1
# pc5 = 1
# pc6 = 1
# pc7 = 1
# pc8 = 1
# pc9 = 1
# pc10 = 1

# def update_pcis(new_pc1 = None,
#                 new_pc2 = None,
#                 new_pc3 = None,
#                 new_pc4 = None,
#                 new_pc5 = None,
#                 new_pc6 = None,
#                 new_pc7 = None,
#                 new_pc8 = None,
#                 new_pc9 = None,
#                 new_pc10 = None):
#     global pc1, pc2, pc3, pc4, pc5, pc6, pc7, pc8, pc9, pc10
#     pc1 = get_val(new_pc1)
#     pc2 = get_val(new_pc2)
#     pc3 = get_val(new_pc3)
#     pc4 = get_val(new_pc4)
#     pc5 = get_val(new_pc5)
#     pc6 = get_val(new_pc6)
#     pc7 = get_val(new_pc7)
#     pc8 = get_val(new_pc8)
#     pc9 = get_val(new_pc9)
#     pc10 = get_val(new_pc10)

# def get_val(pc):
#     if pc == None:
#         return 1 * (10 ** (-15))
#     else:
#         return pc

class Mass:
    def __init__(self, dataset_name, dataset, x_i, class_i):
        self.dataset_name = dataset_name
        self.dataset = dataset
        self.instance = x_i
        self.label = class_i
        self.pcis = get_infos(dataset, x_i, class_i)

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
    df = pd.read_csv("datasets/iris/iris.data",header=None)
    mass = Mass("iris", df, [5.0,3.6,1.4,0.2], "Iris-setosa")
    print(mass.assign_mass())
    # print(ecoli())
    # print(glass())
    # print(haberman())
    # print(ionosphere())
    # print(iris())
    # print(pima())
    # print(sonar())
    # print(thyroid())
    # print(vehicle())
    # print(wdbc())
    # print(wine())
    
    # print('---------------------------------')
    # update_pcis(new_pc1=2, new_pc10=2)
    
    # print(ecoli())
    # print(glass())
    # print(haberman())
    # print(ionosphere())
    # print(iris())
    # print(pima())
    # print(sonar())
    # print(thyroid())
    # print(vehicle())
    # print(wdbc())
    # print(wine())