# Write a python program to determine if the splitted words can be found from the given phrase and print them as well.

def word_split(phrase, list_of_words, output=None):
    # base case
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):], list_of_words, output)

    return output


if __name__ == '__main__':
    phrase = 'themanlovespython'
    split_words = ['the', 'python', 'loves', 'man', 'hello']
    print(word_split(phrase, split_words))
