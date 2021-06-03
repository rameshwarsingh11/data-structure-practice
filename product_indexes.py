# Find the product of all the indexes except the current index in the given list
# Use greedy approach algorithm
# Time complexity: O(n) , Space Complexity: O(n)
def index_prod(list):
  # Create an empty list
  output = [None]*len(list)

  # Forward traversal
  product = 1
  i = 0
  while i < len(list):
    output[i] = product
    product *=list[i]
    i +=1
  print('After forward traversal :::',output)

  # Backward traversal
  product =1

  i=len(list)-1
  while i>=0:
    output[i]*= product
    product*= list[i]
    i-=1
  print('After backward traversal :::', output)
  return output

def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed.')

  else:
    print(wrongTick, 'Test failed.')

if __name__ == '__main__':
  arr = [1,2,3,4,5]
  final_output = index_prod(arr)
  expected = [120, 60, 40, 30, 24]
  check(expected, final_output)
  print('Desired output :::',final_output)