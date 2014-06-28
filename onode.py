from node import Node

class ONode(Node):
    def __init__(self, *args, expectationValue=None):
        Node.__init__(self, *args)
        self.expectationValue = expectationValue

    def getState(self):
        return self.state
