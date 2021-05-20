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


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed.')

  else:
    print(wrongTick, 'Test failed.')


if __name__ == '__main__':
  n = 5
  arr = [1, 2, 3, 4, 5]
  expected = [-1, -1, 6, 24, 60]
  output = findMaxProduct(arr)
  check(expected, output)
  print(output)
