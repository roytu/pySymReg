from link import Link
from activation_functions import fnSigmoid

"""
Node object

Node(state=0)
Creates a node with function op, which takes arbitrarily many values
of the form (state, weight) and returns a number

addThreshold(thresholdInc)
Increase the threshold by some value

addLinkWeight(other, weight)
Add some value to self-to-other link weight

link(other, weight)
Link self to other, where self is input and other is output
Other node is also linked to self

reset()
Reset state to 0 as well as all outputs connected to this node

fire()
Fire this state, processing inputs and setting self.state,
as well as firing all connected output nodes
"""
class Node(object):
    def __init__(self, state=0, threshold=0, activationFn=fnSigmoid(1)):
        self.inputs = []
        self.outputs = []
        self.links = {}
        self.threshold = threshold
        self.activationFn = activationFn
        self.state = state

    def addThreshold(self, thresholdInc):
        self.threshold += thresholdInc

    def addLinkWeight(self, other, weightInc):
        return self.links[other].setWeight(self.links[other].getWeight() + weightInc)

    def link(self, other, weight):
        # self is input, other is output
        self.outputs.append(other)
        other.inputs.append(self)
        link = Link(self, other, weight)
        self.links[other] = link
        other.links[self] = link

    # Propagates signal
    def reset(self):
        self.state = 0
        for output in outputs:
            output.reset()

    # Propagates signal
    def fire(self):
        potential = sum([i.state * self.links[i].getWeight() for i in self.inputs]) + self.threshold
        self.state = self.activationFn(potential)
        for output in self.outputs:
            output.fire()

    # Debugging
    def __str__(self):
        return str(self.state)
