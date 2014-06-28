from math import exp

def fnSigmoid(c):
    """ Logistic function """
    f = lambda x: 1 / (1 + exp(-c * x))
    df = lambda x: c * f(x) * (1 - f(x))
    return (f, df)
