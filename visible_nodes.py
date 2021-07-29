# Find out the left visible number of nodes in a binary tree

import math


class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key


def visible_nodes(root):
    visible_nodes = set()
    max_level = [0]
    leftViewUtil(root, 1, max_level, visible_nodes)
    return len(visible_nodes)


def leftViewUtil(root, level, max_level, visible_nodes):

    # Edge Case
    if root is None:
        return

    # If this is the first node of its level
    if (max_level[0] < level):
        #print(root.val)
        visible_nodes.add(root.val)
        max_level[0] = level

    # Recursive call for left and right subtree
    leftViewUtil(root.left, level + 1, max_level, visible_nodes)
    leftViewUtil(root.right, level + 1, max_level, visible_nodes)
    #print(visible_nodes)
    return visible_nodes

# Driver method
if __name__ == '__main__': 
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)

print(visible_nodes(root))


# Test cases :
def printInteger(n):
  print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1


if __name__ == "__main__":
  root_1 = TreeNode(8)
  root_1.left = TreeNode(3)
  root_1.right = TreeNode(10)
  root_1.left.left = TreeNode(1)
  root_1.left.right = TreeNode(6)
  root_1.left.right.left = TreeNode(4)
  root_1.left.right.right = TreeNode(7)
  root_1.right.right = TreeNode(14)
  root_1.right.right.left = TreeNode(13)
  expected_1 = 4
  output_1 = visible_nodes(root_1)
  check(expected_1, output_1)

  root_2 = TreeNode(10)
  root_2.left = TreeNode(8)
  root_2.right = TreeNode(15)
  root_2.left.left = TreeNode(4)
  root_2.left.left.right = TreeNode(5)
  root_2.left.left.right.right = TreeNode(6)
  root_2.right.left = TreeNode(14)
  root_2.right.right = TreeNode(16)

  expected_2 = 5
  output_2 = visible_nodes(root_2)
  check(expected_2, output_2)
  check(expected_1,output_2)