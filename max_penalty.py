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


print(getTotalPairs([1, 2, 3, 4]))    