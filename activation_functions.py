def fnSigmoid(c):
    return lambda x: 1 / (1 + exp(-c * x))
