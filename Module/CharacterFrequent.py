# Frequency table
frequent_table = {
    'a': 7.07, 'b': 2.05, 'c': 7.06, 'd': 2.67, 'e': 7.89, 'f': 1.32, 'g': 2.36, 'h': 2.01,
    'i': 5.71, 'j': 0.41, 'k': 1.49, 'l': 3.90, 'm': 6.31, 'n': 5.05, 'o': 10.08, 'p': 2.46,
    'q': 0.14, 'r': 6.04, 's': 5.14, 't': 5.19, 'u': 2.97, 'v': 1.11, 'w': 0.94, 'x': 0.47,
    'y': 1.26, 'z': 0.57, '0': 0.11, '1': 0.16, '2': 0.15, '3': 0.09, '4': 0.10, '5': 0.06,
    '6': 0.05, '7': 0.05, '8': 0.06, '9': 0.05, '-': 0.8
}

# Calculate probality of domain
def calculateProbability(text):
    total_count = len(text)
    total_probability = 0

    # Calculate the total probability
    for char in text:
        if char in frequent_table:
            total_probability += frequent_table[char]

    # Calculate the average probability
    return total_probability / total_count if total_count > 0 else 0

''' Result'''
# People's domain
print(calculateProbability("google.com"))
# Botnet's domain
print(calculateProbability("xgxhpyfwlrxdw.com"))
