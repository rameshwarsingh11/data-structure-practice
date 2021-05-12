# Encrypted words in python

def findEncryptedWord(s):
  # Check base case1:
  if len(s) == 0:
    return ''

  # Check base case2:
  if len(s) == 1:
    return s

  #mid is middle number if the length of the string is odd otherwise mid = s[middle-1]
  mid = int(len(s)/2) if len(s) % 2 != 0 else (int((len(s)/2)-1))
  #print(mid)
  #print(s[mid])
  #print(s[0:mid])
  #print(s[mid+1:])
  return s[mid] + findEncryptedWord(s[0:mid]) + findEncryptedWord(s[(mid+1):])


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed!')

  else:
    print(wrongTick, 'Test failed.')


# Driver method :
if __name__ == '__main__':
    expected_1 = 'bac'
    output_1 = findEncryptedWord('abc')
    check(expected_1, output_1)
    print('Encrypted String of [abc] is ::: ', output_1)
    print('"""""""""""""""""""""""')
    expected_2 = 'bacd'
    output_2 = findEncryptedWord('abcd')
    check(expected_2, output_2)
    print('Encrypted String of [abcd] is ::: ', output_2)
    print('"""""""""""""""""""""""')
    print('Encrypted String of [abcxba] is ::: ', findEncryptedWord('abcxcba'))
    print('"""""""""""""""""""""""')
    print('Encrypted String of [FAANGS] is ::: ', findEncryptedWord('FAANGS'))
    print('"""""""""""""""""""""""')
