from inode import INode
from onode import ONode
from network import Network

class Tests(object):
    def printResult(self, expected, actual):
        print("Expected:\n" + expected)
        print("Actual:\n" + str(actual))
        print("")

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
        net.backpropagate(0.9)
        self.printResult("-0.11750185610079725", outputs[0].gradient)
        self.printResult("0", inputs[0].gradient)
        self.printResult("0", inputs[1].gradient)
        self.printResult("0", outputs[0].links[inputs[0]].getWeight())
        self.printResult("-0.10575167049071753", outputs[0].links[inputs[1]].getWeight())
        self.printResult("0", inputs[0].links[outputs[0]].getWeight())
        self.printResult("-0.10575167049071753", inputs[1].links[outputs[0]].getWeight())

    def __init__(self):
        self.testBackpropagation()

if __name__ == "__main__":
    Tests()
