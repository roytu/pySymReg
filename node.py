from random import random
from link import Link
from activation_functions import fnSigmoid

class Node(object):
    """ Constructs a node

    state -- State of the node (default 0)
    bias -- Bias of the node to add to weighted sum (default [-1, 1])
    activationFn -- Activation function, must be nonlinear (default fnSigmoid(1))
    """
    def __init__(self, state=0, bias=None, activationFn=fnSigmoid(1)):
        if bias == None:
            bias = (random() - 0.5) * 2
        self.inputs = []
        self.outputs = []
        self.links = {}
        self.bias = bias
        self.prevDeltaBias = 0
        self.activationFn, self.derivActivationFn = activationFn
        self.state = state

    """ Sets the bias to value.

    Warning: Invalidates delta information!

    bias -- new bias value
    """
    def setBias(self, bias):
        self.bias = bias

    """ Add value to bias and store previous delta

    biasInc -- amount to add to bias (can be negative)
    """
    def addBias(self, biasInc):
        self.prevDeltaBias = biasInc
        self.bias += biasInc

    """ Get value from bias """
    def getBias(self):
        return self.bias

    """ Add value to weight and store previous delta

    other -- other node in link
    weightInc -- amount to add to weight (can be negative)
    """
    def addLinkWeight(self, other, weightInc):
        return self.links[other].addWeight(weightInc)

    """ Get value from weight

    other -- other node in link
    """
    def getLinkWeight(self, other):
        return self.links[other].getWeight()

    """ Link self to other, where self is input and other is output

    other -- output node
    weight -- initial weight (default random [-2, 2])
    """
    def link(self, other, weight=None):
        if weight == None:
            weight = (random() - 0.5) * 4
        # self is input, other is output
        self.outputs.append(other)
        other.inputs.append(self)
        link = Link(self, other, weight)
        self.links[other] = link
        other.links[self] = link

    """ Return input nodes """
    def getInputNodes(self):
        return self.inputs

    """ Return output nodes """
    def getOutputNodes(self):
        return self.outputs

    """ Reset self and all child nodes to state 0 """
    # Propagates signal
    def reset(self):
        self.state = 0
        for output in outputs:
            output.reset()

    """ Computes and stores gradient for backpropagation """
    def computeGradient(self):
        if self.outputs == []:
            # Output neuron
            self.gradient = (self.state - self.expectationValue) * self.derivActivationFn(self.state)
        else:
            self.gradient = sum([output.gradient * self.links[output].getWeight() for output in self.outputs]) * self.derivActivationFn(self.state)

    """ Adjust weights and bias based on calculated gradient """
    def adjust(self, rate, momentumRate=0):
        for other in self.links.keys():
            if other not in self.inputs:
                continue
            link = self.links[other]
            self.addLinkWeight(other, -rate * self.gradient * other.state + momentumRate * link.getPrevDelta())
        self.addBias(-rate * self.gradient + momentumRate * self.prevDeltaBias)

    """ Fires the node and child nodes, setting state """
    # Propagates signal
    def fire(self):
        potential = sum([i.state * self.links[i].getWeight() for i in self.inputs]) + self.bias
        self.state = self.activationFn(potential)
        for output in self.outputs:
            output.fire()

    # Debugging
    def __str__(self):
        return str(self.state)
