from inode import INode
from onode import ONode
from network import Network

from test_utils import testResult

def testOR():
    inputs = [INode(state=0), INode(state=0)]
    outputs = [ONode(expectationValue=0)]
    for i in inputs:
        for o in outputs:
            i.link(o, weight=1)
    net = Network(inputs, outputs)

    for _ in range(10):
        for (i0, i1, ex) in [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]:
            inputs[0].setState(i0)
            inputs[1].setState(i1)
            outputs[0].setExpectation(ex)
            net.fireAll()
            net.backpropagate(0.9)

    # Error rates
    inputs[0].setState(0)
    inputs[1].setState(0)
    net.fireAll()
    testResult(outputs[0].state < 0.5, "OR Gate, with inputs 0 0")

    inputs[0].setState(0)
    inputs[1].setState(1)
    net.fireAll()
    testResult(outputs[0].state > 0.5, "OR Gate, with inputs 0 1")

    inputs[0].setState(1)
    inputs[1].setState(0)
    net.fireAll()
    testResult(outputs[0].state > 0.5, "OR Gate, with inputs 1 0")

    inputs[0].setState(1)
    inputs[1].setState(1)
    net.fireAll()
    testResult(outputs[0].state > 0.5, "OR Gate, with inputs 1 1")

def testAND():
    inputs = [INode(state=0), INode(state=0)]
    outputs = [ONode(expectationValue=0)]
    for i in inputs:
        for o in outputs:
            i.link(o, weight=1)
    net = Network(inputs, outputs)

    for _ in range(10):
        for (i0, i1, ex) in [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]:
            inputs[0].setState(i0)
            inputs[1].setState(i1)
            outputs[0].setExpectation(ex)
            net.fireAll()
            net.backpropagate(0.9)

    # Error rates
    inputs[0].setState(0)
    inputs[1].setState(0)
    net.fireAll()
    testResult(outputs[0].state < 0.5, "AND Gate, with inputs 0 0")

    inputs[0].setState(0)
    inputs[1].setState(1)
    net.fireAll()
    testResult(outputs[0].state < 0.5, "AND Gate, with inputs 0 1")

    inputs[0].setState(1)
    inputs[1].setState(0)
    net.fireAll()
    testResult(outputs[0].state < 0.5, "AND Gate, with inputs 1 0")

    inputs[0].setState(1)
    inputs[1].setState(1)
    net.fireAll()
    testResult(outputs[0].state > 0.5, "AND Gate, with inputs 1 1")

def testXOR():
    inputs = [INode(state=0), INode(state=0)]
    outputs = [ONode(expectationValue=0)]
    for i in inputs:
        for o in outputs:
            i.link(o, weight=1)
    net = Network(inputs, outputs)

    for _ in range(10):
        for (i0, i1, ex) in [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]:
            inputs[0].setState(i0)
            inputs[1].setState(i1)
            outputs[0].setExpectation(ex)
            net.fireAll()
            net.backpropagate(0.9)

    # Error rates
    inputs[0].setState(0)
    inputs[1].setState(0)
    net.fireAll()
    testResult(outputs[0].state < 0.5, "XOR Gate, with inputs 0 0")

    inputs[0].setState(0)
    inputs[1].setState(1)
    net.fireAll()
    testResult(outputs[0].state > 0.5, "XOR Gate, with inputs 0 1")

    inputs[0].setState(1)
    inputs[1].setState(0)
    net.fireAll()
    testResult(outputs[0].state > 0.5, "XOR Gate, with inputs 1 0")

    inputs[0].setState(1)
    inputs[1].setState(1)
    net.fireAll()
    testResult(outputs[0].state < 0.5, "XOR Gate, with inputs 1 1")

def testBooleanLogic():
    testOR()
    testAND()
    testXOR()
