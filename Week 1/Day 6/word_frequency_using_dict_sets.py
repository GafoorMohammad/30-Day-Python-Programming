# Counting word frequency using dictionary and set
sentence = "apple banana apple cherry banana apple"
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # Output: {'apple': 3, 'banana': 2, 'cherry': 1}
