# Reverse a Linked List
# Solve it as in-place solution with constant space complexity ( O(1))
# Perform the traversal linearly ( O(n))
def reverse_linked_list(head):
  current = head
  previous = None
  nextnode = None

  while current: # Loop through the list until you have any nextnode available.
    # copy the value of nextnode reference to a temp variable before overriding as the previous node.
    nextnode = current.nextnode
    current.nextnode = previous
    previous = current
    current = nextnode
  return previous

class Node(object):
  def __init__(self,value):
    self.value = value
    self.nextnode = None
  
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = None

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverse_linked_list(a)
print(' ')

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)