# Check if a binary tree is BST or not

class Node:

  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val = val


INFINITY = float('infinity')
NEG_INFINITY = float('-infinity')


def isBST(tree, minVal=NEG_INFINITY, maxVal=INFINITY):

  # Check base cases:
  if tree is None:
    return True

  if not minVal <= tree.val <= maxVal:
    return False

  return isBST(tree.left, minVal, tree.val) and isBST(tree.right, tree.val, maxVal)


tree = Node(4)
tree.left = Node(5)
tree.right = Node(7)
print(isBST(tree))


# Another inefficient solution : If a binary tree is a Binary Search tree, traversing the tree inorder will sort the tree.
def isBST_with_inorder(tree, lastNode=[NEG_INFINITY]):

    if tree is None:
        return True

    if not isBST_with_inorder(tree.left, lastNode):
      return False

    if tree.val < lastNode[0]:
      return False

    lastNode[0] = tree.val

    return isBST_with_inorder(tree.right, lastNode)


print(isBST_with_inorder(tree))
