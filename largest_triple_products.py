import math
from queue import PriorityQueue


def findMaxProduct(arr):
  q = PriorityQueue()
  final_arr = []
  for i in range(5):
    q.put(-arr[i])

    if q.qsize() < 3:
      final_arr.append(-1)

    else:
      x = q.get()
      y = q.get()
      z = q.get()
      ans = x*y*z
      final_arr.append(-ans)

      q.put(y)
      q.put(x)

  return final_arr


n = 5
arr = [1, 2, 3, 4, 5]
print(findMaxProduct(arr))
