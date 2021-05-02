from collections import Counter


def min_length_substring(s, t):

    # Check base cases :
    if not t or not s or len(s) < len(t):
        return -1

    if len(s) == len(t):
      return 2

    dict_t = Counter(t)
    #print(dict_t)

    required = len(dict_t)
    #print(required)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t so the required sub string can be found.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    #print(filtered_s)

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None  # creating a tuple
    #print(ans)

    # Look for the characters only in the filtered list instead of entire source string. It reduces the search operation need.
    # Now follow the sliding window approach.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1
        #print('window_counts[character] =', window_counts[character])

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]
            #print('character =', character)

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            #print('start', start)
            #print('end', end)

            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)
                #print('ans', ans)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1

        r += 1
    return -1 if ans[0] == float("inf") else len(s[ans[1]: ans[2] + 1])


def printInteger(n):
  print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1


if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

s1 = "dcbefebce"
t1 = "fd"

print(min_length_substring(s1, t1))
