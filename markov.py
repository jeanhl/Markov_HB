from random import choice
import sys

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

    n_gram = int(raw_input("How long is the gram? "))


    for i in range(len(words) - n_gram):
        values = [words[i + n_gram]]
        initial_tuple_key = words[i:(n_gram + i)]
        tuple_key = tuple(initial_tuple_key)
        if tuple_key in chains_dict:
            new_values = chains_dict[tuple_key]
            new_values.append(words[i + n_gram])
            chains_dict[tuple_key] = new_values
        else:
            chains_dict[tuple_key] = values

    print chains_dict
    return chains_dict

#print make_chains(open_and_read_file('green-eggs.txt'))

# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     text = []

#     random_key = choice(chains.keys())
#     n = len(random_key)

#     for i in range(len(random_key)):
#         text.append(random_key[i])

#     while random_key in chains:
#         some_word = choice(chains.get(random_key))
#         text.append(some_word)
#         random_key = tuple(text[-n::])
    
#     return " ".join(text)
        
        
input_path = sys.argv[1] # in terminal, we type in "python markov.py textfile.txt."
                            # [0] is markov.py    [1] is textfile.txt

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
# random_text = make_text(chains)

# print random_text
