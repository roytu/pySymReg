from node import Node

class ONode(Node):
    """ Set the expectation value of the output node """
    def setExpectation(self, expectationValue):
        self.expectationValue = expectationValue

    """ Get the state of the output node """
    def getState(self):
        return self.state
