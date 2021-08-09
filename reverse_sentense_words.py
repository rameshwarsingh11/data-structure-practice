# Perform a sentense word reversal.
# Solution 1 : Using predefined methods.
def words_reversal1(string):
  return " ".join(reversed(string.split()))

print(words_reversal1("We are not alone"))

  # Solution 2 : Using predefined methods.
def words_reversal2(string):
  return " ".join(string.split()[::-1])

print(words_reversal2("This is not the end but a bend"))

# Solution 3 : Loop through the words, split them and add in a stack. Reverse the stack and then print it.
def words_reversal3(string):
  # create an empty list for all the words.
  words = []
  # get length of whole sentense.
  length = len(string)
  spaces = [' ']
  i = 0

  while i <length:
    if string[i] not in spaces:
      word_start = i
      while i < length and string[i] not in spaces:
        i+=1

      words.append(string[word_start:i])

    i +=1

  return " ".join(reversed(words))

print(words_reversal3("Nothing is impossible "))
print(words_reversal3("Impossible is Nothing "))