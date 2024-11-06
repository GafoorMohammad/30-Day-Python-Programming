# Counting word frequency using a dictionary
sentence = "apple banana apple cherry banana apple"
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # Output: {'apple': 3, 'banana': 2, 'cherry': 1}
