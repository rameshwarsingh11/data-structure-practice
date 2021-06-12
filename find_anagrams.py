# Find if two strings are anaagram or not

# Solution 1 : Use predefined python menthods
def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


print(anagram('Listen', 'Silent'))

# Solution 2 : Use dictionary and count each character.


def anagram_another(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Find the edge case first. Like if both the words don't have same number of letters, they can't be anagrams to each other.
    if len(s1) != len(s2):
        return False

    # create a dictionary ( a key value unordered pair, which can't be normally sorted)
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    # Just check what we got.
    print(count)
    return True


def check(expected, output):
    rightTick = '\u2713'
    wrongTick = '\u2717'

    if expected == output:
        print(rightTick, 'Test passed.')

    else:
        print(wrongTick, 'Test failed')


if __name__ == '__main__':
    expected_1 = True
    output_1 = anagram_another('School master', 'The classroom')
    check(expected_1, output_1)
    expected_2 = False
    output_2 = anagram_another('Halloween', 'weenHello')
    check(expected_2, output_2)
