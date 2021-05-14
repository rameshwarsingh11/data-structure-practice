# Find the Nth node from the Last Node in a Linked List.
# Solve it using a left and right pointer processing style.
# Move the right pointer n times faster than the left pointer.
# Like if you need to find the 2nd node form the last then move the right node 2 times faster than the left node towards tail of the list.
def find_nth_node_to_last_node(n, head):
  left_pointer = head
  right_pointer = head

  # setting right pointer n nodes away / faster than the left pointer.
  for i in range(n-1):
    # Check the edge case if we have enough nodes.
    if not right_pointer.nextnode:
      raise LookupError('Error as {n} is larger than the linked list', n)

    # now the right pointer is ntimes faster or away from the left_pointer
    right_pointer = right_pointer.nextnode

  while right_pointer.nextnode:  # Traverse the linked list while the endnode is not reached
    left_pointer = left_pointer.nextnode
    right_pointer = right_pointer.nextnode

  return left_pointer


class Node(object):
  def __init__(self, value):
    self.value = value
    self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f
f.nextnode = None


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed!')

  else:
    print(wrongTick, 'Test failed.')


if __name__ == '__main__':
  expected = 4
  output = find_nth_node_to_last_node(3, a).value
  check(expected, output)
  print(output)
