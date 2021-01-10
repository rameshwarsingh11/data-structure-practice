# Single linked list with cycle check. Mean check if a list is a circular linked lint or not. A node points back to previous node.
# Consider Circular List as a car race track. Move the two pointers along the race track. 
# Move pointer1 as one node at a time and pointer2 as two nodes at a time. It is like two cars are racing with one car is twice as faster than the other car. 
# Now if the pointer2 meets the pointer1 at one stage ( consider the car2 finishes one race lap and crosses car1), then it is a circular Linked List ( track).
# Otherwise the pointer2 will never meet pointer1 and then the List is not circular in that case.

def circular_check(node):
  marker1 = node
  marker2 = node

  while marker2!= None and marker2.nextnode!= None:
    marker1 = marker1.nextnode
    marker2 = marker2.nextnode.nextnode

    if marker2 == marker1:
      # Confirming that there is a cycle.
      return True

  # Otherwise return False to show there is no cycle.
  return False


class Node(object):
  def __init__(self,value):
    self.value = value
    self.nextnode = None

x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z
z.nextnode = x
# z.nextnode = None
print(circular_check(x))
