# Max candies :
"""
You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?
Signature
int maxCandies(int[] arr, int K)
Input
1 ≤ N ≤ 10,000
1 ≤ k ≤ 10,000
1 ≤ arr[i] ≤ 1,000,000,000
Output
A single integer, the maximum number of candies you can eat in k minutes.
Example 1
N = 5 
k = 3
arr = [2, 1, 7, 4, 2]
output = 14
"""
import math
from queue import PriorityQueue


def maxcandies(arr, k):
  candies = 0

  arr.sort(reverse=True)  # in place sorting

  for i in range(0, k):
    candies += arr[0]
    arr[0] = math.floor(arr[0]/2)
    arr.sort(reverse=True)
    #print('Candies eaten in', i+1, 'minute =', candies)
    #print('Array ::', arr)

  return candies


# More efficient method :
# Using PriorityQueue
def max_candies(arr, k):
  total_candies_eaten = 0
  pq = PriorityQueue()

  for candy_pieces in arr:
    pq.put((-candy_pieces, candy_pieces))

  for i in range(k):
    priority, pieces = pq.get()
    #print('pieces',pieces)
    total_candies_eaten += pieces
    #print('Candies eaten in', i+1, 'minute =',total_candies_eaten)
    pieces = math.floor(pieces/2)
    #print('In loop :',pieces)
    pq.put((-pieces, pieces))

  return total_candies_eaten


def check(expected, output):
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if expected == output:
        print(rightTick, 'Test passed!')

    else:
        print(wrongTick, 'Test failed.')

# More optimizes way
def max_candies1(arr, k):
  arr.sort()
  maxValues = arr[-k:]
  maxList = []
  for i in range(len(maxValues)):
    maxList.append(max(maxValues))
    maxValues[maxValues.index(max(maxValues))] //= 2
  return sum(maxList)


# Driver method:
if __name__ == '__main__':
  N = 5  # means 5 candy bags
  k = 3  # means you have total 3 minutes to eat candies
  # array of candy bags. First candy bag has 2 candies, second has 1 candy, third has 7 candies and so on..
  arr = [2, 1, 7, 4, 2]
  output = max_candies1(arr, k)
  expected = 14
  check(expected, output)

  # Another test run :
  n_2, k_2 = 9, 3
  arr_2 = [19, 78, 76, 72, 48, 8, 24, 74, 29]
  expected_2 = 228
  output_2 = max_candies1(arr_2, k_2)
  check(expected_2, output_2)

  # Your task is to find out in 3 minutes how many maximum candies you can eat.
  print('Max candies eaten form the candy bags =', output)
