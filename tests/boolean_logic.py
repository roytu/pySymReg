from test_utils import testResult, testNetwork

def testOR():
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.5], "OR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.5], "OR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.5], "OR Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.5], "OR Gate, with inputs 1 1")
                         ])

def testAND():
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.5], "AND Gate, with inputs 0 0"),
                            ([0, 1], [0], [lambda x: x < 0.5], "AND Gate, with inputs 0 1"),
                            ([1, 0], [0], [lambda x: x < 0.5], "AND Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.5], "AND Gate, with inputs 1 1")
                         ])

def testXOR():
    testNetwork(2, [1], 1, [
                            ([0, 0], [0], [lambda x: x < 0.5], "XOR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.5], "XOR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.5], "XOR Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.5], "XOR Gate, with inputs 1 1")
                         ])

def testBooleanLogic():
    testOR()
    testAND()
    testXOR()
