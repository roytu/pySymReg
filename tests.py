import sys

from inode import INode
from onode import ONode
from network import Network

from tests.backpropagation import testBackpropagation
from tests.boolean_logic import testBooleanLogic

class Tests(object):
    def __init__(self, gui):
        #testBackpropagation(gui)
        testBooleanLogic(gui)

if __name__ == "__main__":
    gui = "gui" in sys.argv
    Tests(gui)
