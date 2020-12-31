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
        print(f'The pair(s) with the sum of {k} : {output}')
    else:
        print('No such pair found.')

# Test the function.
# pair_sum([2,0],8)
pair_sum([2, 2, 4, 5, 7, 9], 9)
# pair_sum([2],4)
