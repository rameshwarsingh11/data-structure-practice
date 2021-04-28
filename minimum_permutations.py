# Minimizing Permutations
"""
Given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.
Signature
int minOperations(int[] arr)
Input
Array arr is a permutation of all integers from 1 to N, N is between 1 and 8
Output
An integer denoting the minimum number of operations required to arrange the permutation in increasing order
Example
If N = 3, and P = (3, 1, 2), we can do the following operations:
Select (1, 2) and reverse it: P = (3, 2, 1).
Select (3, 2, 1) and reverse it: P = (1, 2, 3).
output = 2
"""
# Goal : Find the minimum number of reversing required to make the permutations in the desired increasing order.


def minOperations(arr):
  #print('Original Array :::',arr)
  n = len(arr)
  target = [i+1 for i in range(n)]
  #print('Target array :::',target)
  dictionary = {arr[k]: k for k in range(n)}
  #print('Dictionary of elemnts in the original array with their index positions :::',dictionary)
  count = 0
  for i in range(n):
    # Using dynamic programming
    if arr[i] != i+1:
        index = dictionary[i+1]
        # reverse that sub array and concate. reverse O(n) and concate O(n)
        arr = arr[:i]+list(reversed(arr[i:(index+1)]))
        #print(list(reversed(arr[i:(index+1)])))
        #print(arr)
        if index + 1 < n:
            arr.append(arr[index+1:])
            #print(arr)
        count += 1

        if arr == target:
            return count
  return count


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed!')

  else:
    print(wrongTick, 'Test failed.')


# Driver method :
if __name__ == '__main__':
  arr = [3, 1, 2]
  expected = 2
  output = minOperations(arr)
  check(expected, output)
  print('Minimum number of operations required =', output)
