text = input("введи текст: ")
words = text.split()
word_slovar = {}
for word in words:
    word = word.lower()
if word in word_slovar:
    word_slovar[word] = word_slovar[word] + 1
else:
    word_slovar[word] = 1

print("сколько раз каждое слово встречается:")
print(word_slovar)

ynukalnyewords = len(word_slovar)
print("колво уникальных слов:", ynukalnyewords)