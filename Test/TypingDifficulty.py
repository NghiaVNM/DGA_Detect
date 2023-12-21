from nltk.corpus import wordnet

def typing_difficulty_score(text):
    keys_weight = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                   'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                   't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}  # Assign keys weight
    weight = 0

    # Calculate ratios
    text_length = len(text)
    number_ratio = digit_count(text) / text_length  # Adjust based on your data for number ratio
    hyphen_ratio = text.count('-') / text_length  # Adjust based on your data for hyphen ratio
    # Calculate other ratios (digraph, trigraph, rare word, etc.) - you'll need to implement these functions
    digraph_ratio = calculate_digraph_count(text) / text_length
    rare_word_ratio = calculate_rare_word_count(text) / text_length
    random_word_ratio = calculate_random_word_count(text) / text_length

    # Calculate weight
    weight += sum(keys_weight.get(char.lower(), 0) for char in text)
    weight += number_ratio + hyphen_ratio + digraph_ratio + rare_word_ratio + random_word_ratio
    weight -= consecutive_letters(text)  # Decrease weight for each 3 consecutive letters

    return weight

def digit_count(text):
    count = 0  # Khởi tạo biến để đếm số lượng chữ số

    # Duyệt qua từng ký tự trong chuỗi
    for char in text:
        # Kiểm tra nếu ký tự là chữ số (từ '0' đến '9')
        if char.isdigit():
           count += 1  # Nếu là chữ số, tăng biến đếm lên 1

    return count  # Trả về số lượng chữ số trong chuỗi

def calculate_digraph_count(text):
    digraph_freq = {}  # Tần suất của digraphs

    # Tính tần suất của digraphs
    for i in range(len(text) - 1):
        digraph = text[i:i+2]  # Lấy một cặp ký tự (digraph)
        if len(digraph) == 2:
            if digraph in digraph_freq:
                digraph_freq[digraph] += 1
            else:
                digraph_freq[digraph] = 1

    return len(digraph_freq)


def calculate_rare_word_count(text):
    # Function to calculate rare word count
    # Implement this function based on your algorithm to count rare words in the text
    pass


def calculate_random_word_count(text):
    words = text.split()
    random_word_count = 0

    for word in words:
        # Loại bỏ dấu câu và chữ số trong từ
        word = word.translate(str.maketrans('', '', string.punctuation)).lower()
        word = ''.join([i for i in word if not i.isdigit()])

        # Kiểm tra xem từ có trong WordNet hay không
        synsets = wordnet.synsets(word)
        if not synsets:
            random_word_count += 1

    return random_word_count

def consecutive_letters(text):
    # Function to calculate consecutive letters count
    count = 0
    for i in range(len(text) - 2):
        if text[i] == text[i + 1] == text[i + 2]:
            count += 1
    return count


# Example usage:
input_text = "Your input text here"
difficulty_score = typing_difficulty_score(input_text)
print(f"Typing Difficulty Score: {difficulty_score}")
