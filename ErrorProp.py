# Function for computing error through error propagation using sympy
from sympy import diff, symbols, sqrt

def errorProp(expr):
    terms = []
    for i in expr.args():
        terms.append(diff(f,i)**2 + symbols('s_' + i)**2)
    return sqrt(sum(terms))
