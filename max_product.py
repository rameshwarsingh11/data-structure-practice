# Find the max product and pair from a given array of integers

def max_product(arr, n):

    if (n < 2):
        print("Sorry, no such pairs exists")
        return 0

    a = arr[0]
    b = arr[1]

    # Find each possible pair with max product
    for i in range(0, n):

        for j in range(i + 1, n):
            if (arr[i] * arr[j] > a * b):
                a = arr[i]
                b = arr[j]
    max_product = a*b
    print('Max product is :', max_product)
    print("Max product pair is {", a, ",", b, "}",
          )
    return max_product


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed!')

  else:
    print(wrongTick, 'Test failed.')


if __name__ == '__main__':
  expected1 = 20
  arr1 = [1, 2, 3, 4, 5]
  n1 = len(arr1)
  output1 = max_product(arr1, n1)
  check(expected1, output1)
  print(output1)

  arr2 = [-1, -2, 1, 3, -6]
  expected2 = 12
  n2 = len(arr2)
  output2 = max_product(arr2, n2)
  check(expected2, output2)
  print(output2)
