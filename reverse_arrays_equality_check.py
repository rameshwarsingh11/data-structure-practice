# Find if two arrays are equal by reversing the other array multiple times.
def are_they_equal(array_a, array_b):
  # using Greedy Algorithm
  n = len(array_a)
  for i in range(n):
      if array_a[i] != array_b[i]:
          try:
             
              index_in_b = array_b.index(array_a[i])
            
              array_b = reverse_array(array_b,i,index_in_b)
          except ValueError:
              return False

  return array_b == array_a


def reverse_array(array_b,start,end):
    # find target in array_b and reverse it to target_index position

    arr = array_b[start:end+1]
    arr.reverse()
    array_b = array_b[:start]
    array_b = array_b+arr

    return array_b

if __name__ == "__main__":
    print(are_they_equal([1,2,3,4],[2,3,4,1]))
    #print(are_they_equal([3,5,6], [8,9,5,6,3]))
    #print(are_they_equal([3,5,6], [8,9,5,6]))
