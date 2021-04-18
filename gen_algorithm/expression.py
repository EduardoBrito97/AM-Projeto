import parser

class Expression:
    def __init__(self, left, right=None, operation=None):
        self.left = left
        self.right = right
        self.operation = operation

    def eval(self):
        if self.right == None:
            return str(self.left)
        elif self.left == None:
            return str(self.right)
        else:
            return '(' + self.left.eval() + ')' + self.operation + '(' + self.right.eval() + ')'
expr = Expression( Expression(Expression('y'), Expression(2), '**'), Expression('x'), '+')