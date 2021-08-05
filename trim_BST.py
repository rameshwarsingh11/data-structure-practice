# Trim a Binary Search Tree
# Post trimming the tree must be a valid Binary Search Tree
# Solution : Using post order traversal. Time complexity : O(n) where n is the number of nodes in the tree.

def trim_BST(tree, minVal, maxVal):
  if not tree:
    return

  # Recursive call
  # Post order traversal
  tree.left = trim_BST(tree.left, minVal, maxVal)
  tree.right = trim_BST(tree.right, minVal, maxVal)

  if minVal <= tree.val <= maxVal:
    return tree

  # Discard left tree
  if tree.val <= minVal:
    return tree.right

  # Discard right tree
  if tree.val > maxVal:
    return tree.left


class Node:

  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val = val

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)
print(root.val)
print((trim_BST(root, 6, 13)).val)
print((trim_BST(root, 7, 13)).val)
print((trim_BST(root, 8, 10)).val)
