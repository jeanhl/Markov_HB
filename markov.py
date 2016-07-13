from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    opened_file = open(file_path).read()

    return opened_file


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains_dict = {}

    # this will give us a list of individual words
    words = text_string.split()

    for i in range(len(words) - 2):
        values = [words[i + 2]]

        if (words[i], words[i + 1]) in chains_dict:
            new_values = chains_dict[(words[i], words[i + 1])]
            new_values.append(words[i + 2])
            chains_dict[(words[i], words[i + 1])] = new_values
        else:
            chains_dict[(words[i], words[i + 1])] = values

    return chains_dict

print make_chains(open_and_read_file('green-eggs.txt'))

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = []

    random_key = choice(chains.keys())

    text.extend([random_key[0],random_key[1]])

    while random_key in chains:
        some_word = choice(chains.get(random_key))
        text.append(some_word)
        random_key = (text[-2], text[-1])
    
    return " ".join(text)
        
        
input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
