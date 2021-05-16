# Find out array pair sum problem :
# Solution : Big O notation : O(n)
def pair_sum(array, k):
    # Do an edge case check first. In case if there are less than two elements in the array then stop processing.
    if len(array) < 2:
        print('Sorry. The array is not complete.')
        return

    # Create a set to keep track of number that we visit.
    seen = set()
    output = set()

    for num in array:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min)(num, target), (max)(num, target)))

    if len(output) > 0:
        return output
    else:
        print('No such pair found.')

# Test the function.


def check(expected, output):
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if expected == output:
        print(rightTick, 'Test passed.')

    else:
        print(wrongTick, 'Test failed.')


if __name__ == '__main__':
    expected = {(4, 5), (2, 7)}
    k = 9
    arr = [2, 2, 4, 5, 7, 9]
    output = pair_sum(arr, k)
    check(expected, output)
    print(output)
