from inode import INode
from onode import ONode
from network import Network

from tests.backpropagation import testBackpropagation
from tests.boolean_logic import testBooleanLogic

class Tests(object):
    def __init__(self):
        testBackpropagation()
        testBooleanLogic()

if __name__ == "__main__":
    Tests()
