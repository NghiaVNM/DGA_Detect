# Giả định UNIGRAMS là một từ điển có thông tin về tần suất xuất hiện của các từ trong ngữ liệu
UNIGRAMS = {
    'word1': 15000,
    'word2': 8000,
    'word3': 5000,
    # ...
}

def rareness_of_domain_words(words):
    random_word_count = 0
    rare_word_count = 0
    common_word_count = 0

    for word in words:
        if UNIGRAMS.get(word) is None:  # Nếu từ không có trong unigram
            random_word_count += 1
        elif UNIGRAMS.get(word) < 10000:  # Nếu từ có tần suất xuất hiện ít hơn 10,000 lần
            rare_word_count += 1
        else:  # Nếu từ có tần suất xuất hiện lớn hơn hoặc bằng 10,000 lần
            common_word_count += 1

    return random_word_count, rare_word_count, common_word_count

# Example usage:
input_words = ['word1', 'word2', 'word3', 'word4', 'word5']
random_count, rare_count, common_count = rareness_of_domain_words(input_words)
print(f"Random Words: {random_count}")
print(f"Rare Words: {rare_count}")
print(f"Common Words: {common_count}")
