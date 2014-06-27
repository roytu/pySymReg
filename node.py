from link import Link
from activation_functions import fnSigmoid

"""
Node object

Node(op, state=0)
Creates a node with function op, which takes arbitrarily many values
of the form (state, weight) and returns a number

addThreshold(thresholdInc)
Increase the threshold by some value

link(other, weight)
Link self to other, where self is input and other is output
Other node is also linked to self

setLinkWeight(other, weight)
Set weight of link from self to other

getLinkWeight(other)
Get weight of link from self to other

reset()
Reset state to 0 as well as all outputs connected to this node

fire()
Fire this state, processing inputs and setting self.state,
as well as firing all connected output nodes
"""
class Node(object):
    def __init__(self, op, state=0, threshold=0, activationFn=fnSigmoid(1)):
        self.inputs = []
        self.outputs = []
        self.links = {}
        self.threshold = threshold
        self.activationFn = activationFn
        self.op = op
        self.state = state

    def addThreshold(self, thresholdInc):
        self.threshold += thresholdInc

    def link(self, other, weight):
        # self is input, other is output
        self.outputs.append(other)
        other.inputs.append(self)
        link = Link(self, other, weight)
        self.links[other] = link
        other.links[self] = link

    def getLinkWeight(self, other):
        return self.links[other].getWeight()

    def setLinkWeight(self, other, weight):
        self.links[other].setWeight(weight)

    # Propagates signal
    def reset(self):
        self.state = 0
        for output in outputs:
            output.reset()

    # Propagates signal
    def fire(self):
        self.state = self.op(*[(i.state, self.getLinkWeight(i)) for i in self.inputs])
        for output in self.outputs:
            output.fire()

    # Debugging
    def __str__(self):
        return str(self.state)
