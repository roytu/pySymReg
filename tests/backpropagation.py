from inode import INode
from onode import ONode
from network import Network

from test_utils import printResult

def testBackpropagation():
    """ Basic backpropagation test """
    inputs = [INode(state=0), INode(state=1)]
    outputs = [ONode()]
    for i in inputs:
        for o in outputs:
            i.link(o, weight=0)
    net = Network(inputs, outputs)

    printResult("Input: [  0  1  ]\nOutput: [  0  ]", net)
    net.fireAll()
    printResult("Input: [  0  1  ]\nOutput: [  0.5  ]", net)
    net.backpropagate(0.9)
    printResult("-0.11750185610079725", outputs[0].gradient)
    printResult("0", inputs[0].gradient)
    printResult("0", inputs[1].gradient)
    printResult("0", outputs[0].links[inputs[0]].getWeight())
    printResult("-0.10575167049071753", outputs[0].links[inputs[1]].getWeight())
    printResult("0", inputs[0].links[outputs[0]].getWeight())
    printResult("-0.10575167049071753", inputs[1].links[outputs[0]].getWeight())
