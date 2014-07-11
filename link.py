class Link(object):
    """ Constructs a bidirectional link between two nodes with a certain weight
    No distinction between input / output

    node1 -- first node
    node2 -- second node
    weight -- weight of link
    """
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.prevDeltaWeight = 0

    """ Returns node 1 """
    def getNode1(self):
        return self.node1

    """ Returns node 2 """
    def getNode2(self):
        return self.node2

    """ Returns weight """
    def getWeight(self):
        return self.weight

    """ Sets weight to value

    weight -- weight of link """
    def setWeight(self, weight):
        self.weight = weight

    """ Adds value to weight and stores previous delta

    weightInc -- amount to add to weight
    """
    def addWeight(self, weightInc):
        self.prevDeltaWeight = weightInc
        self.weight += weightInc

    """ Gets previous weight delta """
    def getPrevDelta(self):
        return self.prevDeltaWeight

    # Debugging
    def __repr__(self):
        return str(self.weight)
