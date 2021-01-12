# Find out if list of words can be formed from a given string

def check_matching_words(phrase, list_of_words, output = None):
  if output is None:
    output = [] # Creating an empty list in the first recrusion. This will avoid overriding of output list in each recursion loop.

  for word in list_of_words:
    if phrase.startswith(word):
      output.append(word)

      return check_matching_words(phrase[len(word):],list_of_words, output)

  return output

print(check_matching_words('impossible',['possible','i','m']))