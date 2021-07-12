from abc import ABC, abstractmethod


class Expressions(ABC):

    @abstractmethod
    def value(self, x):
        pass

    @abstractmethod
    def derivative(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Const(Expressions):
    def __init__(self, integer):
        self.integer = integer

    def value(self, x):
        return self.integer

    def derivative(self):
        return Const(0)

    def __str__(self):
        return "(" + str(self.integer) + ")"


class Var(Expressions):

    def __init__(self, symbol):
        self.symbol = symbol

    def value(self, x):
        return x

    def derivative(self):
        return Const(1)

    def __str__(self):
        return "(" + self.symbol + ")"


class Operator(Expressions):

    def __init__(self, *args):
        if len(args) == 2:
            self.left, self.right = args[0], args[1]
        elif len(args) == 1:
            self.exponent = args[0]

    @abstractmethod
    def name(self):
        pass

    def __str__(self):
        if self.name() == "e^":
            return "(" + self.name() + str(self.exponent) + ")"
        else:
            return "(" + str(self.left) + self.name() + str(self.right) + ")"
