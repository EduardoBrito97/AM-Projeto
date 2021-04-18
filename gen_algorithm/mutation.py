import random

from expression import Expression

pc1s = ['pc1', 'pc2', 'pc3', 'pc4', 'pc5', 'pc6', 'pc7', 'pc8', 'pc9', 'pc10']
operations = ['+', '-', '/', '*', '**']

def mutation(expr):
    depth = random.randint(1, 10)
    mutated_expr = expr
    parent_expr = None
    for _ in range(depth):
        left_or_right = random.randint(0, 2)
        chosen_expr = None
        
        if left_or_right % 2 == 0:
            chosen_expr = expr.right
        else:
            chosen_expr = expr.left
        
        if chosen_expr != None and type(chosen_expr) == Expression:
            parent_expr = expr
            mutated_expr = chosen_expr
        else:
            break

    eliminate_or_change = random.randint(0, 2):
    if eliminate_or_change % 2 == 0:
