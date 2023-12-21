from nltk.corpus import wordnet
import string
import RarenesssOfDomainWord  # Import your custom module

# File path to the data.txt file
file_path = '../Dataset/Alexa_Benign.txt'

# Read data from the file and create a list of domains
with open(file_path, 'r') as file:
    data_lines = file.readlines()

# Convert data lines to lowercase and strip extra whitespace
domains_list = [line.strip().lower() for line in data_lines]

def typing_difficulty_score(text):
    keys_weight = {
        'a': 3, 'b': 4, 'c': 6, 'd': 3, 'e': 2, 'f': 3, 'g': 4, 'h': 5, 'i': 2, 'j': 4,
        'k': 5, 'l': 4, 'm': 3, 'n': 4, 'o': 2, 'p': 3, 'q': 3, 'r': 3, 's': 5, 't': 3,
        'u': 2, 'v': 5, 'w': 3, 'x': 7, 'y': 4, 'z': 6
    }

    weight = 0
    text_length = len(text)

    number_ratio = digit_count(text) / text_length
    hyphen_ratio = text.count('-') / text_length

    digraph_ratio = calculate_digraph_count(text) / text_length
    rare_word_ratio = RarenesssOfDomainWord.calculate_rarity_of_domain(text, domains_list)
    random_word_ratio = calculate_random_word_count(text) / text_length

    weight += sum(keys_weight.get(char.lower(), 0) for char in text)
    weight += number_ratio + hyphen_ratio + digraph_ratio + rare_word_ratio + random_word_ratio
    weight -= consecutive_letters(text)

    return weight

def digit_count(text):
    count = sum(1 for char in text if char.isdigit())
    return count

def calculate_digraph_count(text):
    digraph_freq = {}

    for i in range(len(text) - 1):
        digraph = text[i:i+2]
        if len(digraph) == 2:
            digraph_freq[digraph] = digraph_freq.get(digraph, 0) + 1

    return len(digraph_freq)

def calculate_random_word_count(text):
    random_word_count = 0

    for word in text.split():
        word = ''.join(filter(lambda x: x.isalpha(), word.lower()))
        synsets = wordnet.synsets(word)
        if not synsets:
            random_word_count += 1

    return random_word_count

def consecutive_letters(text):
    count = sum(1 for i in range(len(text) - 2) if text[i] == text[i + 1] == text[i + 2])
    return count

# Example usage:
input_text = "uit.edu.vn"
difficulty_score = typing_difficulty_score(input_text)
print(f"Typing Difficulty Score: {difficulty_score}")
