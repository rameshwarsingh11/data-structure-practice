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
# Output is still wrong. Needs to be corrected.
import math
from queue import PriorityQueue


def maxCandies(arr, k):
  candies = 0
  pq = PriorityQueue()

  for candies_in_bag in arr:
    pq.put(candies_in_bag)

  #l = list(pq.queue)
  for candybag in pq.queue:
    print(candybag)
  #print('Candy bags array :',l)

  for i in range(k):
    pieces = pq.get()
    #print('pieces', pieces)
    candies += pieces
    #print('candies', candies)
    pieces = math.floor(pieces/2)
    #print('In loop :', pieces)
    pq.put(pieces)

  return candies


if __name__ == '__main__':
    N = 5
    k = 3
    arr = [2, 1, 7, 4, 2]
    print(maxCandies(arr, k))
