from nltk.corpus import wordnet
import string

import RarenesssOfDomainWord

keys_weight = {
    'a': 3, 'b': 4, 'c': 6, 'd': 3, 'e': 2, 'f': 3, 'g': 4, 'h': 5, 'i': 2, 'j': 4,
    'k': 5, 'l': 4, 'm': 3, 'n': 4, 'o': 2, 'p': 3, 'q': 3, 'r': 3, 's': 5, 't': 3,
    'u': 2, 'v': 5, 'w': 3, 'x': 7, 'y': 4, 'z': 6,
    '0': 4, '1': 5, '2': 6, '3': 6, '4': 6, '5': 6, '7': 6, '8': 6, '9': 6,
    '-': 6
}

def keys_weight_score(text):
    return sum(keys_weight.get(char.lower(), 0) for char in text)
'''
Test :
print(keys_weight_score("google.com"))  # People
print(keys_weight_score("uj9gz24qeeni1lby2l214idsv6.net"))  # Botnet
'''

def digit_count(text):
    count = sum(1 for char in text if char.isdigit())
    return count
'''
Test :
print(digit_count("google.com"))    # People
print(digit_count("uj9gz24qeeni1lby2l214idsv6.net"))    # Botnet
'''

def digraph_and_triagraph_count(text):
    digraph_freq = {}
    triagraph_freq = {}

    for i in range(len(text) - 1):
        digraph = text[i:i+2]
        if len(digraph) == 2:
            digraph_freq[digraph] = digraph_freq.get(digraph, 0) + 1

    for i in range(len(text) - 2):
        triagraph = text[i:i+3]
        if len(triagraph) == 3:
            triagraph_freq[triagraph] = triagraph_freq.get(triagraph, 0) + 1

    return len(digraph_freq) + len(triagraph_freq)
'''
Test :
print(digraph_and_triagraph_count("google.com"))    # People
print(digraph_and_triagraph_count("uj9gz24qeeni1lby2l214idsv6.net"))    # Botnet
'''

def random_word_count(text):
    count = 0

    for word in text.split():
        word = ''.join(filter(lambda x: x.isalpha(), word.lower()))
        synsets = wordnet.synsets(word)
        if not synsets:
            count += 1

    return count
'''
Test : 
print(random_word_count("google.com"))      # People
print(random_word_count("uj9gz24qeeni1lby2l214idsv6.net"))     # Botnet
'''

def consecutive_letters(text):
    count = sum(1 for i in range(len(text) - 2) if text[i] == text[i + 1] == text[i + 2])
    return count
'''
Test :
print(consecutive_letters("google.com"))    # People
print(consecutive_letters("uj9gz24qeeeni1lby2l214idsv6.net"))   # Botnet
'''


def typing_difficulty_score(domain):
    weight = 0
    text_length = len(domain)

    # Calculate number's ratio
    number_ratio = digit_count(domain) / text_length

    # Calculate hyphen's ratio
    hyphen_ratio = domain.count('-') / text_length

    # Calculate digraph and trigraph ratio
    digraph_ratio = digraph_and_triagraph_count(domain) / text_length

    # Calculate rare word ratio
    rare_word_ratio = RarenesssOfDomainWord.calculate_rarity_of_domain(domain)

    # Calculate random word ratio
    random_word_ratio = random_word_count(domain) / text_length

    # Calculate key weight score
    weight += keys_weight_score(domain)

    weight += number_ratio + hyphen_ratio + digraph_ratio + rare_word_ratio + random_word_ratio
    weight -= consecutive_letters(domain)

    return weight
'''
Test :
print(typing_difficulty_score("google.com"))    # People
print(typing_difficulty_score("uj9gz24qeeni1lby2l214idsv6.net"))    # Botnet
'''