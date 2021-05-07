# Find number of ones in a sub array
# Using greedy approach.
#Solution: Time complexity : O(n) and Space complexity : O(1)

def find_no_ones(start, end, arr):
  count = 0
  for val in range(start, end):
    #print(arr[val])
    if arr[val] == 1:
      count += 1
  return count


start_1 = 0
end_1 = 3
start_2 = 2
end_2 = 5
arr = [0, 0, 1, 0, 1, 0]
print(find_no_ones(start_1, end_1, arr))
print(find_no_ones(start_2, end_2, arr))
