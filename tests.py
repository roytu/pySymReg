from inode import INode
from onode import ONode
from network import Network

class Tests(object):
    def __init__(self):
        def add(*args):
            return sum(map(lambda x: x[0] * x[1], args))
        inputs = [INode(add, x) for x in [1, 2, 3]]
        outputs = [ONode(add, x) for x in [0] * 3]
        for i in inputs:
            for o in outputs:
                i.link(o, 3)
        net = Network(inputs, outputs)
        print(net)
        net.fireAll()
        print(net)

if __name__ == "__main__":
    Tests()
