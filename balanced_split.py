# Split an array into two equal subs arrays such that the sum of both the individual arrays is equal and one array value(s) must be greater than the other sub array.

def balancedSplitExists(arr):
    if not arr:
        return False
    target = sum(arr)
    if target % 2 != 0:
        return False
    target /= 2

    def canSplit(cur_arr, lo_sum):
        if not cur_arr:
            return False
        pivot = cur_arr[0]
        sum, lower_array, higher_array = 0, [], []
        for x in cur_arr:
            if x < pivot:
                sum += x
                lower_array.append(x)
            elif x == pivot:
                sum += x
            else:
                higher_array.append(x)
        if target == sum + lo_sum:
            return True
        elif sum < target:
            return canSplit(higher_array, sum + lo_sum)
        else:
            return canSplit(lower_array, lo_sum)
    return canSplit(arr, 0)


print(balancedSplitExists([1, 1, 5, 7]))
print(balancedSplitExists([12, 7, 6, 7, 6]))
