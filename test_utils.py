from inode import INode
from onode import ONode
from node import Node
from network import Network, makeNetwork
from gui.gui import Gui

from activation_functions import fnSigmoid

def printResult(expected, actual):
    print("Expected:\n" + expected)
    print("Actual:\n" + str(actual))
    print("")

def testNetwork(inputCount, hiddensCount, outputCount, patterns, initSetup=None, cycles=1000, learnRate=0.9, momentumRate=0.4, activationFn=fnSigmoid(1), stopEarly=False, gui=False):
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
    activationFn -- activation function for neurons (default fnSigmoid(1))
    stopEarly -- stop when all patterns succeed (default False)
    gui -- boolean for gui testing (default False)
    """
    net = makeNetwork(inputCount, hiddensCount, outputCount, initSetup, activationFn)
    
    for cycle in range(1, cycles + 1):
        if gui:
            Gui.drawNetwork(net)
        if net.train(patterns, learnRate, momentumRate, stopEarly):
            break
        
    # Testing
    for (inputStates, _, conds, failureString) in patterns:
        for (s, i) in zip(inputStates, net.getInputNodes()):
            i.setState(s)
        net.fireAll()
        print("Input " + str(inputStates) +", Output " + str(net.getOutputNodes()[0].state))
        for (out, cond) in zip(map(lambda o: o.state, net.getOutputNodes()), conds):
            if not testResult(cond(out), failureString):
                return
    print("Passed after {0} cycles".format(cycle))

def testResult(condition, failureString):
    if not condition:
        print("TEST FAILED: " + failureString)
        return False
    return True
