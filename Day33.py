"""Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return ( 'Node(' + repr(self.val) + ', '
                         + repr(self.left) + ', '
                         + repr(self.right) + ')' )

    def __eq__(self, other):
        if isinstance(other, Node):
            return ( self.val == other.val and
                     self.left == other.left and
                     self.right == other.right )
        return False

    def __hash__(self):
        return hash((self.val, self.left, self.right))

serialise = repr
deserialise = eval

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialise(serialise(node)).left.left.val == 'left.left'
assert deserialise(serialise(node)) == node
assert hash(deserialise(serialise(node))) == hash(node)
