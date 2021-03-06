# Merge Sort in python

def merge_sort(arr):

  # Checking the base case here. If the arr has 1 element only, it is already sorted. Otherwise, we will sort it recursivly
  if len(arr) > 1:
    # Calculate the mid point of the list
    mid = int(len(arr)/2)
    # Now split the list into two halfs
    lefthalf = arr[:mid]  # using python's slice operation
    righthalf = arr[mid:]

    # Call mergesort recursively on left and right halfs
    merge_sort(lefthalf)
    merge_sort(righthalf)

    # initialize three different index tracker.
    i = 0  # For the lefthalf
    j = 0  # For the righthalf
    k = 0  # To define final sorted list

    # while loop to take care of mid point
    # To check we are still in the left & right halfs
    while i < len(lefthalf) and j < len(righthalf):
      if lefthalf[i] < righthalf[j]:
        arr[k] = lefthalf[i]
        i += 1

      else:
        arr[k] = righthalf[j]
        j += 1

      k += 1

    # while loop to merge the left sublist
    while i < len(lefthalf):
      arr[k] = lefthalf[i]
      i += 1
      k += 1

      # while loop to merge the right sublist
    while j < len(righthalf):
      arr[k] = righthalf[j]
      j += 1
      k += 1
  return arr
  #print('Now merging ::', arr)


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if expected == output:
    print(rightTick, 'Test passed')

  else:
    print(wrongTick, 'Test failed.')


if __name__ == '__main__':
  arr = [11, 2, 3, 56, 7, 78, 91, 1]
  expected = [1, 2, 3, 7, 11, 56, 78, 91]
  output = merge_sort(arr) # It is an in place sorting. No new array was created to make the algorithm cost efficient.
  check(expected, output)
  print(output)
