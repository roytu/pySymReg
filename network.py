from queue import Queue

class Network(object):
    """
    Create a network given a set of input and output nodes
    Hidden nodes are linked among each node and not handled by the Network object

    Returns: Network object
    """
    def __init__(self, inputNodes, outputNodes):
        self.inputNodes = inputNodes
        self.outputNodes = outputNodes

    """
    Fire the network; that is, get all input layer's output nodes to probe for input
    """
    def fireAll(self):
        for i in self.inputNodes:
            for ii in i.outputs:
                ii.fire()

    """
    Reset the state of all nodes
    """
    def resetAll(self):
        for i in self.inputNodes:
            i.reset()

    """
    Error propagation
    """
    def backpropagate(self):
        allNodes = self.nodes()
        for node in allNodes:
            node.computeGradient()
        for node in allNodes:
            node.adjust(0.9)

    """
    Gets a list of all nodes from output to input
    """
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
