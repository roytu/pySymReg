from node import Node

class INode(Node):
    """ Set the state of the input node """
    def setState(self, state):
        self.state = state
