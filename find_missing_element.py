# Find out the missing element from the second array which is formed by reshuffling of the first array.
# Solution 1 : Time complexity of this solution : O(nlogn)
import collections


def find_missing_element1(array1, array2):
    # Sort the arrays to carefully check the duplicates
    array1.sort()
    array2.sort()

    # Now compare elements of these sorted arrays
    # zip method makes tuples for the given arrays. it returns a list of tuples.
    for num1, num2 in zip(array1, array2):
        if num1 != num2:
            return num1

    return array1[-1]


print('Solution 1 :', find_missing_element1(
    [1, 2, 3, 4, 5, 6, 7], [3, 4, 6, 7, 1, 2, ]))

# Solution 2: Using a Hashtable.


def find_missing_element2(array1, array2):
    # Default Dictionary is like ordinary dictionary with a difference that if the key is not present it will not throw error.
    d = collections.defaultdict(int)

    # Add a count for every instance of the array
    for num in array2:
        d[num] += 1

    for num in array1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1


print('Solution 2 :', find_missing_element2(
    [1, 2, 3, 4, 5, 6, 7], [3, 4, 6, 7, 1, 2, ]))

# Solution 3 : Find the sum of numbers of the first and second array. Then deduct sum of second array from that of first array and the result is the missing number. This approach is good for only small array sizes. For long array sizes or very large numbers, it will cause an overflow.
# And not suitable to arrays with floating numbers.


# Solution 4 :
# Linear Time O(n) complexity and Constant space O(1).
# Use Exclusive OR ( XOR ) which does bit comparions.

def find_missing_element3(array1, array2):
    result = 0
    # array1+array will create a join list of elements. It is like concatenating the arrays.
    for num in array1+array2:
        result ^= num
        print(result)

    return result


def check(expected, output):
    rightTick = '\u2713'
    wrongTick = '\u2717'

    if expected == output:
        print(rightTick, 'Test passed.')

    else:
        print(wrongTick, 'Test failed.')


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [3, 4, 6, 7, 1, 2]
    arr3 = [3, 4, 6, 7, 1, 2, 3]
    expected_1 = 5
    expected_2 = 4
    expected_3 = 4
    output_1 = find_missing_element1(arr1, arr2)
    output_2 = find_missing_element1(arr1, arr3)
    output_3 = find_missing_element1(arr2, arr3)
    check(expected_1, output_1)
    check(expected_2, output_2)
    check(expected_3, output_3)
    print(output_1)
    print(output_2)
    print(output_3)
