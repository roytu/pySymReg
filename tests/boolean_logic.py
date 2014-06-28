from test_utils import testNetwork

def testNOT():
    """ NOT Gate. 1 input, 1 output """
    print("Testing NOT...")
    testNetwork(1, [], 1, [
                            ([0], [1], [lambda x: x > 0.5], "NOT Gate, with input 0"),
                            ([1], [0], [lambda x: x < 0.5], "NOT Gate, with input 1"),
                         ], stopEarly=True)

def testNOR():
    """ NOR Gate. 2 inputs, 1 output """
    print("Testing NOR...")
    testNetwork(2, [], 1, [
                            ([0, 0], [1], [lambda x: x > 0.5], "NOR Gate, with inputs 0 0"),
                            ([0, 1], [0], [lambda x: x < 0.5], "NOR Gate, with inputs 0 1"),
                            ([1, 0], [0], [lambda x: x < 0.5], "NOR Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.5], "NOR Gate, with inputs 1 1")
                         ], stopEarly=True)
   

def testOR():
    """ OR Gate. 2 inputs, 1 output """
    print("Testing OR...")
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.5], "OR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.5], "OR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.5], "OR Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.5], "OR Gate, with inputs 1 1")
                         ], stopEarly=True)

def testAND():
    """ AND Gate. 2 inputs, 1 output """
    print("Testing AND...")
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.5], "AND Gate, with inputs 0 0"),
                            ([0, 1], [0], [lambda x: x < 0.5], "AND Gate, with inputs 0 1"),
                            ([1, 0], [0], [lambda x: x < 0.5], "AND Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.5], "AND Gate, with inputs 1 1")
                         ], stopEarly=True)

def testNAND():
    """ NAND Gate. 2 inputs, 1 output """
    print("Testing NAND...")
    testNetwork(2, [], 1, [
                            ([0, 0], [1], [lambda x: x > 0.5], "NAND Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.5], "NAND Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.5], "NAND Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.5], "NAND Gate, with inputs 1 1")
                         ], stopEarly=True)

def testXOR():
    """ XOR Gate. 2 inputs, 2 hidden, 1 output """
    print("Testing XOR...")
    testNetwork(2, [2], 1, [
                            ([0, 0], [0], [lambda x: x < 0.5], "XOR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.5], "XOR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.5], "XOR Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.5], "XOR Gate, with inputs 1 1")
                         ], cycles=1000, stopEarly=True)

def testBooleanLogic():
    testOR()
    testAND()
    testXOR()
    testNOR()
    testNOT()
    testNAND()
