word1 = input("введи первое слово: ").lower()
word2 = input("введи второе слово: ").lower()

if len(word1) != len(word2):
    print(False)
else:
    count1 = {}
    for letter in word1:
        if letter in count1:
            count1[letter] = count1[letter] + 1
        else:
            count1[letter] = 1

    count2 = {}
    for letter in word2:
        if letter in count2:
            count2[letter] = count2[letter] + 1
        else:
            count2[letter] = 1

    if count1 == count2:
        print(True)
    else:
        print(False)