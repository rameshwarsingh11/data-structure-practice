# Given an array of positive integers. Choose any two numbers, find their sum and replace these two numbers in the array. This sum to be treated as a cost. Now repeat this process and find the max cost.

def getTotalPairs(arr):

  arr.sort(reverse=True)
  #print('Sorted array :', arr)
  penalty = 0
  for i in range(len(arr)-1):
    val = arr[i] + arr[i+1]
    penalty += val
    arr[i+1] = val
    #print(arr[i+1])
  return penalty


def check(expected, output):
    rightTick = '\u2713'
    wrongTick = '\u2717'

    if expected == output:
        print(rightTick, 'Test passed !')

    else:
        print(wrongTick, 'Test failed.')


if __name__ == '__main__':
  expected = 26
  output = getTotalPairs([1, 2, 3, 4])
  check(expected, output)
  print(output)
