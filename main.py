"""
Mateusz Sikorski
30.01.2021
Program do wizualizacji i wyliczania wartości oraz pochodnych wyrażeń matematycznych

Trening obiektowości
"""


from math_expressions.Expressions import Const, Var
from math_expressions.Operations import Power, Sum, Div, Multi, Diff

if __name__ == '__main__':
    a = Const(5)
    b = Var("x")
    c = Div(Sum(Multi(Const(7), Power(b, Const(2))), b), Diff(Power(b, Const(3)), b))
    d = c.derivative()
    print(c)
    print(d)
    print(c.value(2))
    print(d.value(2))
