

def findSignatureCounts(arr):
  L = len(arr)
  res = [0] * L
  # set of visited students
  visited = set()
  for i in range(len(arr)):
    if i not in visited:
      j = i
      # the students of the same group as student i
      group = set([i])
      # keep passing the yearbook until it goes back to i
      while arr[j]-1 != i:
        j = arr[j]-1
        group.add(j)
      # update the visited set
      visited.update(group)
      for k in group:
        res[k] = len(group)
  return res


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed!')

  else:
    print(wrongTick, 'Test failed')


if __name__ == '__main__':
    expected = [2, 2]
    arr = [2, 1]
    output = findSignatureCounts(arr)
    check(expected, output)
    print(output)
