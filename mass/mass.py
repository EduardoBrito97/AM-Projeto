pc1 = 1
pc2 = 1
pc3 = 1
pc4 = 1
pc5 = 1
pc6 = 1
pc7 = 1
pc8 = 1
pc9 = 1
pc10 = 1

def update_pcis(new_pc1 = None,
                new_pc2 = None,
                new_pc3 = None,
                new_pc4 = None,
                new_pc5 = None,
                new_pc6 = None,
                new_pc7 = None,
                new_pc8 = None,
                new_pc9 = None,
                new_pc10 = None):
    global pc1, pc2, pc3, pc4, pc5, pc6, pc7, pc8, pc9, pc10
    pc1 = get_val(new_pc1)
    pc2 = get_val(new_pc2)
    pc3 = get_val(new_pc3)
    pc4 = get_val(new_pc4)
    pc5 = get_val(new_pc5)
    pc6 = get_val(new_pc6)
    pc7 = get_val(new_pc7)
    pc8 = get_val(new_pc8)
    pc9 = get_val(new_pc9)
    pc10 = get_val(new_pc10)

def get_val(pc):
    if pc == None:
        return 1 * (10 ** (-15))
    else:
        return pc

def ecoli():
    expr1 = (pc5 + pc9) ** 0.5
    expr2 = 107.0172 * (expr1/pc4)
    return 3.2749 - expr2

def glass():
    expr1 = 6.0104 * (10 ** 15) * (pc9 ** 0.5) * (pc3-pc7)
    expr2 = (2.8823 * (10 ** 17) * pc6) + (5.3608 * (10 ** 17))
    return (expr1/expr2) + 3.7029

def haberman():
    expr1 = 8.5856 * (10 ** (-7))
    expr2 = (pc7 ** 2) / (pc6 ** 2)
    return 1.13845 - (expr1 * expr2)

def ionosphere():
    return (0.0115 * pc10) + 0.3545

def iris():
    return (0.5095 * pc5) - (0.0089 * pc8) + 3.8569 + (0.0027 * pc1) + (0.0471  * pc6 * pc9)

def pima():
    expr1 = 4.6357 * (10 ** (-8)) * (pc7 ** 2) * pc9
    expr2 = 6.7395 * (10 ** (-8)) * (pc7 ** 2)
    return expr1 + expr2 + 0.0014

def sonar():
    return 1.4015 - (0.0269 * (pc8 ** (1/2)))

def thyroid():
    return 2.8450 - (0.0133 * pc2)

def vehicle():
    return 2.5963 - (0.1954 * pc10)

def wdbc():
    return 0.8835 - (0.0638 * pc5)

def wine():
    return (0.9508 * pc1) + 0.7208

if __name__ == "__main__":
    print(ecoli())
    print(glass())
    print(haberman())
    print(ionosphere())
    print(iris())
    print(pima())
    print(sonar())
    print(thyroid())
    print(vehicle())
    print(wdbc())
    print(wine())
    
    print('---------------------------------')
    update_pcis(new_pc1=2, new_pc10=2)
    
    print(ecoli())
    print(glass())
    print(haberman())
    print(ionosphere())
    print(iris())
    print(pima())
    print(sonar())
    print(thyroid())
    print(vehicle())
    print(wdbc())
    print(wine())