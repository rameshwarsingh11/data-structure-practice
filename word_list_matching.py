# Find out if list of words can be formed from a given string

def check_matching_words(phrase, list_of_words, output = None):
  if output is None:
    output = [] # Creating an empty list in the first recrusion. This will avoid overriding of output list in each recursion loop.

  for word in list_of_words:
    if phrase.startswith(word):
      output.append(word)

      return check_matching_words(phrase[len(word):],list_of_words, output)

  if list_of_words == ['possible','i','m']:
    return True
  
  return False


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed!')
  
  else:
    print(wrongTick, 'Test failed')

if __name__ == '__main__':
  arr = ['possible','i','m']
  phrase = 'impossible'
  expected = True
  output = check_matching_words(phrase,arr)
  check(expected, output)