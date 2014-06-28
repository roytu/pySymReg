from random import random
from link import Link
from activation_functions import fnSigmoid

"""
Node object

Node(state=0, bias=0, activationFn=fnSigmoid(1))
Creates a node.

addBias(biasInc)
Increase the bias by some value

addLinkWeight(other, weight)
Add some value to self-to-other link weight.

link(other, weight)
Link self to other, where self is input and other is output, with the given weight
Other node is also linked to self.

computeGradient()
Compute gradient for backpropagation phase.

adjust(rate)
Backpropagation; adjust weights and bias.  Rate must be greater than 0.

reset()
Reset state to 0 for this node as well as all outputs connected to this node.

fire()
Fire this state, processing inputs and setting self.state, as well as firing all connected output nodes.
"""

class Node(object):
    def __init__(self, state=0, bias=0, activationFn=fnSigmoid(1)):
        self.inputs = []
        self.outputs = []
        self.links = {}
        self.bias = bias
        self.prevDeltaBias = 0
        self.activationFn, self.derivActivationFn = activationFn
        self.state = state

    def addBias(self, biasInc):
        self.prevDeltaBias = biasInc
        self.bias += biasInc

    def addLinkWeight(self, other, weightInc):
        return self.links[other].setWeight(self.links[other].getWeight() + weightInc)

    @property
    def potential(self):
        return sum([i.state * self.links[i].getWeight() for i in self.inputs]) + self.bias

    def link(self, other, weight=None):
        if weight == None:
            weight = (random() - 0.5) * 4
        # self is input, other is output
        self.outputs.append(other)
        other.inputs.append(self)
        link = Link(self, other, weight)
        self.links[other] = link
        other.links[self] = link

    def getInputNodes(self):
        return self.inputs

    # Propagates signal
    def reset(self):
        self.state = 0
        for output in outputs:
            output.reset()

    def computeGradient(self):
        if self.outputs == []:
            # Output neuron
            self.gradient = (self.expectationValue - self.state) * self.derivActivationFn(self.state)
        else:
            self.gradient = sum([output.gradient * self.links[output].getWeight() for output in self.outputs]) * self.derivActivationFn(self.state)

    def adjust(self, rate, momentumRate=0):
        for other in self.links.keys():
            if other not in self.inputs:
                continue
            link = self.links[other]
            link.addWeight(rate * self.gradient * other.state + momentumRate * link.getPrevDelta())
        self.addBias(rate * self.gradient + momentumRate * self.prevDeltaBias)

    # Propagates signal
    def fire(self):
        self.state = self.activationFn(self.potential)
        for output in self.outputs:
            output.fire()

    # Debugging
    def __str__(self):
        return str(self.state)
