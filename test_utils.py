from inode import INode
from onode import ONode
from node import Node
from network import Network

def printResult(expected, actual):
    print("Expected:\n" + expected)
    print("Actual:\n" + str(actual))
    print("")

def testNetwork(inputCount, hiddensCount, outputCount, patterns, cycles=10, learnRate=0.9):
    """ Tests a network based on the number of nodes provided and the test patterns.

    Does nothing if succeeds, else prints failure string.

    inputCount -- number of input nodes
    hiddensCount -- list of number of hidden nodes for respective layers
    outputCount -- number of output nodes
    patterns -- training patterns ([inputs], [expected outputs], [conditions], [failure string])
    cycles -- number of epochs to train for (default 10)
    learnRate -- rate of learning (default 0.9)
    """
    inputs = [INode() for _ in range(inputCount)]
    hiddens = [[Node() for _ in range(hn)] for hn in hiddensCount]
    outputs = [ONode() for _ in range(outputCount)]

    # Link each layer
    layers = [inputs] + hiddens + [outputs]
    for (layer0, layer1) in zip(layers, layers[1:]):
        for l0 in layer0:
            for l1 in layer1:
                l0.link(l1, weight=1)
    net = Network(inputs, outputs)

    # Training
    for _ in range(cycles):
        for (inputStates, exps, _, _) in patterns:
            for (s, i) in zip(inputStates, inputs):
                i.setState(s)
            for (e, o) in zip(exps, outputs):
                o.setExpectation(e)
            net.fireAll()
            net.backpropagate(learnRate)

    # Testing
    for (inputStates, _, conds, failureString) in patterns:
        for (s, i) in zip(inputStates, inputs):
            i.setState(s)
        net.fireAll()
        for (out, cond) in zip(map(lambda o: o.state, outputs), conds):
            testResult(cond(out), failureString)

def testResult(condition, failureString):
    if not condition:
        print("TEST FAILED: " + failureString)
