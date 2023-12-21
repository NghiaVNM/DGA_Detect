from nltk.corpus import wordnet
import string

def calculate_random_word_ratio(text):
    words = text.split()
    total_words = len(words)
    random_word_count = 0

    for word in words:
        # Loại bỏ dấu câu và chữ số trong từ
        word = word.translate(str.maketrans('', '', string.punctuation)).lower()
        word = ''.join([i for i in word if not i.isdigit()])

        # Kiểm tra xem từ có trong WordNet hay không
        synsets = wordnet.synsets(word)
        if not synsets:
            random_word_count += 1

    random_word_ratio = random_word_count / total_words if total_words > 0 else 0
    return random_word_ratio

# Sử dụng hàm với một đoạn văn bản
input_text = "google.com"
ratio = calculate_random_word_ratio(input_text)
print(f"Random Word Ratio: {ratio:.2f}")
