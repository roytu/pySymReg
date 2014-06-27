from inode import INode
from onode import ONode
from network import Network

class Tests(object):
    def __init__(self):
        inputs = [INode(x) for x in [1, 2, 3]]
        outputs = [ONode(x) for x in [0] * 3]
        for i in inputs:
            for o in outputs:
                i.link(o, 0)
        net = Network(inputs, outputs)
        print(net)
        net.fireAll()
        print(net)

if __name__ == "__main__":
    Tests()
