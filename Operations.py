from abc import abstractmethod
from math import e, log

from math_expressions.Expressions import Operator, Const, Var


class Sum(Operator):

    def value(self, x):
        return self.left.value(x) + self.right.value(x)

    def derivative(self):
        return Sum(self.left.derivative(), self.right.derivative())

    def name(self):
        return "+"


class Diff(Operator):

    def value(self, x):
        return self.left.value(x) - self.right.value(x)

    def derivative(self):
        return Diff(self.left.derivative(), self.right.derivative())

    def name(self):
        return "-"


class Multi(Operator):

    def value(self, x):
        return self.left.value(x) * self.right.value(x)

    def derivative(self):
        return Sum(Multi(self.left.derivative(), self.right),
                   Multi(self.left, self.right.derivative()))

    def name(self):
        return "*"


class Div(Operator):

    def value(self, x):
        return self.left.value(x) / self.right.value(x)

    def derivative(self):
        return Div(
            Diff(Multi(self.left.derivative(), self.right),
                 Multi(self.left, self.right.derivative())),
            Power(self.right, Const(2)))

    def name(self):
        return "/"


class Power(Operator):

    def value(self, x):
        return self.left.value(x) ** self.right.value(x)

    def derivative(self):
        if isinstance(self.left, Var) and isinstance(self.right, Const):
            return Multi(self.right, Power(self.left, Diff(self.right, Const(1))))
        elif isinstance(self.left, Var) and isinstance(self.right, Var):
            return Multi(Power(self.left, self.left), Sum(nLog(self.left), Const(1)))
        else:
            return Multi(Power(self.left, self.right), nLog(self.left))

    def name(self):
        return "^"


class Exp(Operator):

    def value(self, x):
        return e ** self.exponent.value(x)

    def derivative(self):
        return Exp(self.exponent)

    def name(self):
        return "e^"


class Logarithms(Operator):

    @abstractmethod
    def name(self):
        pass

    def __str__(self):
        if self.name() == "ln":
            return "(" + self.name() + str(self.exponent) + ")"
        else:
            return "(" + self.name() + str(self.left) + str(self.right) + ")"


class Log(Logarithms):

    def value(self, x):
        return log(self.right.value(x), self.left.value(x))

    def derivative(self):
        return Div(Log(self.left, e), self.right)

    def name(self):
        return "log"


class nLog(Logarithms):

    def value(self, x):
        return log(self.exponent.value(x))

    def derivative(self):
        return Div(Const(1), self.exponent)

    def name(self):
        return "ln"
