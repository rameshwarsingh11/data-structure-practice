
def countDistinctTriangles(arr):
    # Create a counter of unique elements
    counter = set()

    # loop through the given triangle list
    for triangle in arr:
        counter.add(tuple(sorted(triangle)))

    return len(counter)


def check(expected, output):
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if expected == output:
        print(rightTick,'Test passed !')

    else:
         print(wrongTick,'Test failed.')


# Driver method :
if __name__ == '__main__':
    arr_1 = [[1, 2, 3], [2, 3, 1], [3, 4, 1]]
    output_1 = countDistinctTriangles(arr_1)
    expected_1 = 2
    check(expected_1, output_1)
    print('Number of distinct triangles : ', output_1)
