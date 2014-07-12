from inode import INode
from onode import ONode
from node import Node

from activation_functions import fnSigmoid
from queue import Queue

class Network(object):
    """ Create a network given a set of input and output nodes
    Hidden nodes are linked among each node and not handled by the Network object

    Returns: Network object
    """
    def __init__(self, inputNodes, outputNodes):
        self.inputNodes = inputNodes
        self.outputNodes = outputNodes

    """ Fire the network; that is, get all input layer's output nodes to probe for input """
    def fireAll(self):
        for i in self.inputNodes:
            for ii in i.outputs:
                ii.fire()

    """ Reset the state of all nodes """
    def resetAll(self):
        for i in self.inputNodes:
            i.reset()

    """ Error propagation """
    def backpropagate(self, rate, momentumRate):
        allNodes = self.nodes()
        for node in allNodes:
            node.computeGradient()
        for node in allNodes:
            node.adjust(rate, momentumRate)

    """ Gets a list of all nodes from output to input """
    def nodes(self):
        frontier = Queue()
        for outputNode in self.outputNodes:
            frontier.put(outputNode)
        closed = []
        while not frontier.empty():
            node = frontier.get()
            for inputNode in node.getInputNodes():
                if inputNode not in closed:
                    frontier.put(inputNode)
            closed.append(node)
        return closed

    """ Gets a list of list of nodes, by layer, from input to output

    e.g. [[inputNodes], [hidden1Nodes], [hidden2Nodes], [outputNodes]]

    Assumes all nodes in one layer are connected to all nodes in linked layers
    """
    def nodesByLayer(self):
        layers = []
        layer = self.inputNodes
        while len(layer) > 0:
            layers.append(layer)
            layer = layer[0].getOutputNodes()
        return layers

    """ Get input nodes """
    def getInputNodes(self):
        return self.inputNodes

    """ Get output nodes """
    def getOutputNodes(self):
        return self.outputNodes

    """ Trains a network based on the number of nodes provided and the test patterns.

    Returns whether the network is fully trained or not (only if stopEarly=True)

    patterns -- training patterns ([inputs], [expected outputs], [conditions], [failure string])
    learnRate -- rate of learning (default 0.9)
    momentumRate -- weight of previous deltas (default 0.4)
    stopEarly -- stop when all patterns succeed (default False)
    """
    def train(self, patterns, learnRate=0.9, momentumRate=0.4, stopEarly=False):
        for (inputStates, exps, _, _) in patterns:
            for (s, i) in zip(inputStates, self.inputNodes):
                i.setState(s)
            for (e, o) in zip(exps, self.outputNodes):
                o.setExpectation(e)
            self.fireAll()
            self.backpropagate(learnRate, momentumRate)

        # Stop when all patterns succeed
        if stopEarly:
            allPatternsTrained = True
            for (inputStates, _, conds, _) in patterns:
                for (s, i) in zip(inputStates, self.inputNodes):
                    i.setState(s)
                self.fireAll()
                for (out, cond) in zip(map(lambda o: o.state, self.outputNodes), conds):
                    if not cond(out):
                        allPatternsTrained = False
                        break
            if allPatternsTrained:
                return True
        return False

    def __str__(self):
        s = "Input: "
        s += "[  "
        for i in self.inputNodes:
            s += str(i) + "  "
        s += "]\n"
        s += "Output: "
        s += "[  "
        for o in self.outputNodes:
            s += str(o) + "  "
        s += "]"
        return s

def makeNetwork(inputCount, hiddensCount, outputCount, initSetup=None, activationFn=fnSigmoid(1)):
    """ Returns a network based on the number of nodes provided and the test patterns.

    inputCount -- number of input nodes
    hiddensCount -- list of number of hidden nodes for respective layers
    outputCount -- number of output nodes
    initSetup -- initial node weights / biases (default None, random) e.g. ([[[input1hiddens], [input2hiddens] ...], [[hidden1outputs], [hidden2outputs] ...]], [[hidden1biases], [hidden2biases], ... [outputbiases]])
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
                    l1.setBias(initBias(i, i1))
    return Network(inputs, outputs)
