
class Node:
  def __init__(self, val):
    self.data = val
    self.next = None

def reverse(head):

    node = head
    output = []

    while node:
        is_even = node.data % 2 == 0
        if is_even:  # If node value is even, push it into the output stack.
            output.append(node)
            #print(node.data)

        if not is_even or node.next is None:  # Odd case. Start popping values from the stack.
              left = 0
              right = len(output)-1 # pointers are more optimal than pop()
              while len(output) > 1 and left < right: # while there is atleast one element in output stack and the pointers haven't crossed each others
                output[left].data, output[right].data = output[right].data, output[left].data # swapping node values
                left +=1
                right -= 1
                #output.pop(0) --> Will take O(N) to remove 1st element, as you need to shift everything to the left  
                #output.pop(-1) --> will take O(1) to remove last element 
                output = [] # O(N) # Clear the stack.
        node = node.next # Go to next node

    return head


def printLinkedList(head):
  print('[', end='')
  while head != None:
    print(head.data, end='')
    head = head.next
    if head != None:
      print(' ', end='')
  print(']', end='')

test_case_number = 1

def check(expectedHead, outputHead):
  global test_case_number
  tempExpectedHead = expectedHead
  tempOutputHead = outputHead
  result = True
  while expectedHead != None and outputHead != None:
    result &= (expectedHead.data == outputHead.data)
    expectedHead = expectedHead.next
    outputHead = outputHead.next

  if not(outputHead == None and expectedHead == None):
    result = False

  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printLinkedList(tempExpectedHead)
    print(' Your output: ', end='')
    printLinkedList(tempOutputHead)
    print()
  test_case_number += 1

def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead

if __name__ == "__main__":
  head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
  expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
  output_1 = reverse(head_1)
  check(expected_1, output_1)

  head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
  expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
  output_2 = reverse(head_2)
  check(expected_2, output_2)
  