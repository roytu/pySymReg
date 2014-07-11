from test_utils import testNetwork
from activation_functions import fnTanhShifted, fnStep

def testNOT():
    """ NOT Gate. 1 input, 1 output """
    print("Testing NOT...")
    testNetwork(1, [], 1, [
                            ([0], [1], [lambda x: x > 0.9], "NOT Gate, with input 0"),
                            ([1], [0], [lambda x: x < 0.1], "NOT Gate, with input 1"),
                         ], stopEarly=True)

def testNOR():
    """ NOR Gate. 2 inputs, 1 output """
    print("Testing NOR...")
    testNetwork(2, [], 1, [
                            ([0, 0], [1], [lambda x: x > 0.9], "NOR Gate, with inputs 0 0"),
                            ([0, 1], [0], [lambda x: x < 0.1], "NOR Gate, with inputs 0 1"),
                            ([1, 0], [0], [lambda x: x < 0.1], "NOR Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.1], "NOR Gate, with inputs 1 1")
                         ], stopEarly=True)
   

def testOR():
    """ OR Gate. 2 inputs, 1 output """
    print("Testing OR...")
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.1], "OR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.9], "OR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.9], "OR Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.9], "OR Gate, with inputs 1 1")
                         ], stopEarly=True)

def testAND():
    """ AND Gate. 2 inputs, 1 output """
    print("Testing AND...")
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.1], "AND Gate, with inputs 0 0"),
                            ([0, 1], [0], [lambda x: x < 0.1], "AND Gate, with inputs 0 1"),
                            ([1, 0], [0], [lambda x: x < 0.1], "AND Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.9], "AND Gate, with inputs 1 1")
                         ], stopEarly=True)

def testNAND():
    """ NAND Gate. 2 inputs, 1 output """
    print("Testing NAND...")
    testNetwork(2, [], 1, [
                            ([0, 0], [1], [lambda x: x > 0.9], "NAND Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.9], "NAND Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.9], "NAND Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.1], "NAND Gate, with inputs 1 1")
                         ], stopEarly=True)

def testXOR():
    """ XOR Gate. 2 inputs, 2 hidden, 1 output """
    print("Testing XOR...")
    testNetwork(2, [2], 1, [
                            ([0, 0], [0], [lambda x: x < 0.1], "XOR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.9], "XOR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.9], "XOR Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.1], "XOR Gate, with inputs 1 1")
                         ], initSetup=(
                                        [[[1, 2], [1, 2]], [[-1], [0.85]]]
                                      , [[0, 0], [0]]
                            ), stopEarly=True)
#                            ), cycles=10000, momentumRate=0, stopEarly=True, activationFn=fnStep())

def testBooleanLogic():
    #testOR()
    #testAND()
    #testNOR()
    #testNOT()
    #testNAND()
    testXOR()
