def printResult(expected, actual):
    print("Expected:\n" + expected)
    print("Actual:\n" + str(actual))
    print("")

def testNetwork(inputCount, hiddensCount, outputCount, patterns, trainingCycles=10, learnRate=0.9):
    """ Tests a network based on the number of nodes provided and the test patterns. """
    inputs = [INode()] * inputCount
    hiddens = [[Node()] * hn for hn in hiddensCount]
    outputs = [ONode(expectationValue=0)]

    # Link each layer
    layers = [inputs] + hiddens + [outputs]
    for (layer0, layer1) in zip(layers, layers[1:]):
        for l0 in layer0:
            for l1 in layer1:
                l0.link(l1, weight=1)
    net = Network(inputs, outputs)

    # Training
    for _ in range(trainingCycles):
        for (inps, exps, _, _) in patterns:
            for inp in inps:
                inputs[inp].setState(inps[inp])
            for exp in exps:
                outputs[exp].setExpectation(exps)
            net.fireAll()
            net.backpropagate(learnRate)

    # Testing
    for (inps, _, conds, failureString) in patterns:
        for inp in inps:
            inputs[inp].setState(inps[inp])
        net.fireAll()
        for (out, cond) in zip(map(lambda o: o.state, outputs), conds):
            testResult(cond(out), failureString)

def testResult(condition, failureString):
    if not condition:
        print("TEST FAILED: " + failureString)
