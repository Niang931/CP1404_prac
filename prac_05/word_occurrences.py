from operator import itemgetter

text = input("Enter a text:").split()
print(text)
word_to_count = {}
word_count = 0

for word in text:
    word_to_count[word] = text.count(word)

word_to_count = sorted(word_to_count.items(), key=itemgetter(0,1))
print(word_to_count)
