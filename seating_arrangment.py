# Seating arrangement problem to find mimimum awkwardness :

def minOverallAwkwardness(arr):
  if len(arr) < 4:
    return max(arr) - min(arr)
  arr.sort()
  print(arr)
  left = right = 0
  diff = float('-inf')
  print(diff)
  for i in range(1, len(arr), 2):  # range(start,stop,step)
    if i + 1 < len(arr):
      diff = max(diff, max(arr[i] - arr[left], arr[i+1] - arr[right]))
      print('Inside loop :', diff)
      left = i
      right = i + 1
    else:
      print('Within else : diff:', diff)
      print(i)
      print(left)
      print(right)
      diff = max(diff, max(arr[i] - arr[left], arr[i] - arr[right]))
  return diff


print(minOverallAwkwardness([5,10,6,8]))