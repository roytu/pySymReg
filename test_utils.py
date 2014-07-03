from inode import INode
from onode import ONode
from node import Node
from network import Network

from activation_functions import fnSigmoid

def printResult(expected, actual):
    print("Expected:\n" + expected)
    print("Actual:\n" + str(actual))
    print("")

def testNetwork(inputCount, hiddensCount, outputCount, patterns, initSetup=None, cycles=1000, learnRate=0.9, momentumRate=0.4, activationFn=fnSigmoid(1), stopEarly=False):
    """ Tests a network based on the number of nodes provided and the test patterns.

    Does nothing if succeeds, else prints failure string.

    inputCount -- number of input nodes
    hiddensCount -- list of number of hidden nodes for respective layers
    outputCount -- number of output nodes
    initSetup -- initial node weights / biases (default None, random) e.g. ([[[input1hiddens], [input2hiddens] ...], [[hidden1outputs], [hidden2outputs] ...]], [[hidden1biases], [hidden2biases], ... [outputbiases]])
    patterns -- training patterns ([inputs], [expected outputs], [conditions], [failure string])
    cycles -- number of epochs to train for (default 10)
    learnRate -- rate of learning (default 0.9)
    momentumRate -- weight of previous deltas (default 0.4)
    stopEarly -- stop when all patterns succeed (default False)
    """
    inputs = [INode(activationFn=activationFn) for _ in range(inputCount)]
    hiddens = [[Node(activationFn=activationFn) for _ in range(hn)] for hn in hiddensCount]
    outputs = [ONode(activationFn=activationFn) for _ in range(outputCount)]

    def initWeight(i, i0, i1):
        if initSetup == None:
            return None
        else:
            return initSetup[0][i][i0][i1]

    def initBias(i, i0):
        return initSetup[1][i][i0]

    # Link each layer
    layers = [inputs] + hiddens + [outputs]
    for ((layer0, layer1), i) in zip(zip(layers, layers[1:]), range(len(layers))):
        for (l0, i0) in zip(layer0, range(len(layer0))):
            for (l1, i1) in zip(layer1, range(len(layer1))):
                l0.link(l1, weight=initWeight(i, i0, i1))
                if initSetup != None:
                    l1.setBias(initBias(i, i0))
    net = Network(inputs, outputs)

    # Training
    for cycle in range(1, cycles + 1):
        for (inputStates, exps, _, _) in patterns:
            for (s, i) in zip(inputStates, inputs):
                i.setState(s)
            for (e, o) in zip(exps, outputs):
                o.setExpectation(e)
            net.fireAll()
            net.backpropagate(learnRate, momentumRate)

        # Stop when all patterns succeed
        if stopEarly:
            allPatternsTrained = True
            for (inputStates, _, conds, _) in patterns:
                for (s, i) in zip(inputStates, inputs):
                    i.setState(s)
                net.fireAll()
                for (out, cond) in zip(map(lambda o: o.state, outputs), conds):
                    if not cond(out):
                        allPatternsTrained = False
                        break
            if allPatternsTrained:
                break

    # Testing
    for (inputStates, _, conds, failureString) in patterns:
        for (s, i) in zip(inputStates, inputs):
            i.setState(s)
        net.fireAll()
        print("Input " + str(inputStates) +", Output " + str(outputs[0].state))
        for (out, cond) in zip(map(lambda o: o.state, outputs), conds):
            if not testResult(cond(out), failureString):
                return
    print("Passed after {0} cycles".format(cycle))

def testResult(condition, failureString):
    if not condition:
        print("TEST FAILED: " + failureString)
        return False
    return True
