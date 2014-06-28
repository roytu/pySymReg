from inode import INode
from onode import ONode
from network import Network

class Tests(object):
    def printResult(self, expected, actual):
        print("Expected:\n" + expected)
        print("\n")
        print("Actual:\n" + str(actual))
        print("\n")

    def testBackpropagation(self):
        inputs = [INode(state=0), INode(state=1)]
        outputs = [ONode(expectationValue=0)]
        for i in inputs:
            for o in outputs:
                i.link(o, weight=0)
        net = Network(inputs, outputs)

        self.printResult("Input: [  0  1  ]\nOutput: [  0  ]", net)
        net.fireAll()
        self.printResult("Input: [  0  1  ]\nOutput: [  0.5  ]", net)

    def __init__(self):
        self.testBackpropagation()

if __name__ == "__main__":
    Tests()
