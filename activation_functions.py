from math import exp, tanh, cosh

def fnSigmoid(c):
    """ Logistic function """
    f = lambda x: 1 / (1 + exp(-c * x))
    df = lambda x: c * f(x) * (1 - f(x))
    return (f, df)

def fnTanhShifted():
    """ Hyperbolic tangent from [0, 1] centered at 0.5 """
    f = lambda x: tanh(x) / 2 + 0.5
    df = lambda x: pow(1 / cosh(x), 2) / 2
    return (f, df)

def fnStep():
    """ Step function. Should not be used for propagation """
    f = lambda x: 0 if x < 0 else 1
    df = lambda _: 0
    return (f, df)
