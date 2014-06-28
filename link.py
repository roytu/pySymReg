"""
Link object between two nodes.
Bidirectional link; no distinction between input or output.

Link(node1, node2, weight)
node1 - Node object
node2 - Node object
weight - number

getNode1()
Returns node 1

getNode2()
Returns node 2

getWeight()
Returns weight

setWeight(weight)
Sets weight
Returns nothing

addWeight(weightInc)
Add weight
Returns nothing
"""
class Link(object):
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.prevDeltaWeight = 0

    def getNode1(self):
        return self.node1

    def getNode2(self):
        return self.node2

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def addWeight(self, weightInc):
        self.prevDeltaWeight = weightInc
        self.weight += weightInc

    def getPrevDelta(self):
        return self.prevDeltaWeight
