from test_utils import testNetwork
from activation_functions import fnTanhShifted, fnStep
from test_metadata import TestMetadata

def testNOT(gui=False):
    """ NOT Gate. 1 input, 1 output """
    print("Testing NOT...")
    testNetwork(1, [], 1, [
                            ([0], [1], [lambda x: x > 0.9], "NOT Gate, with input 0"),
                            ([1], [0], [lambda x: x < 0.1], "NOT Gate, with input 1"),
                         ], stopEarly=True, gui=gui, metadata=TestMetadata("NOT Gate"))

def testNOR(gui=False):
    """ NOR Gate. 2 inputs, 1 output """
    print("Testing NOR...")
    testNetwork(2, [], 1, [
                            ([0, 0], [1], [lambda x: x > 0.9], "NOR Gate, with inputs 0 0"),
                            ([0, 1], [0], [lambda x: x < 0.1], "NOR Gate, with inputs 0 1"),
                            ([1, 0], [0], [lambda x: x < 0.1], "NOR Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.1], "NOR Gate, with inputs 1 1")
                         ], stopEarly=True, gui=gui, metadata=TestMetadata("NOR Gate"))
   

def testOR(gui=False):
    """ OR Gate. 2 inputs, 1 output """
    print("Testing OR...")
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.1], "OR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.9], "OR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.9], "OR Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.9], "OR Gate, with inputs 1 1")
                         ], stopEarly=True, gui=gui, metadata=TestMetadata("OR Gate"))

def testAND(gui=False):
    """ AND Gate. 2 inputs, 1 output """
    print("Testing AND...")
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.1], "AND Gate, with inputs 0 0"),
                            ([0, 1], [0], [lambda x: x < 0.1], "AND Gate, with inputs 0 1"),
                            ([1, 0], [0], [lambda x: x < 0.1], "AND Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.9], "AND Gate, with inputs 1 1")
                         ], stopEarly=True, gui=gui, metadata=TestMetadata("AND Gate"))

def testNAND(gui=False):
    """ NAND Gate. 2 inputs, 1 output """
    print("Testing NAND...")
    testNetwork(2, [], 1, [
                            ([0, 0], [1], [lambda x: x > 0.9], "NAND Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.9], "NAND Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.9], "NAND Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.1], "NAND Gate, with inputs 1 1")
                         ], stopEarly=True, gui=gui, metadata=TestMetadata("NAND Gate"))

def testXOR(gui=False):
    """ XOR Gate. 2 inputs, 2 hidden, 1 output """
    print("Testing XOR...")
    testNetwork(2, [2], 1, [
                            ([0, 0], [0], [lambda x: x < 0.1], "XOR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.9], "XOR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.9], "XOR Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.1], "XOR Gate, with inputs 1 1")
                         ], cycles=3000, stopEarly=True, gui=gui, metadata=TestMetadata("XOR Gate"))

def testBooleanLogic(gui=False):
    testOR(gui)
    testAND(gui)
    testNOR(gui)
    testNOT(gui)
    testNAND(gui)
    testXOR(gui)
