word = input()
words = []
while word != "":
    if word not in words:
        words.append(word)
    word = input()
for i in range(len(words)):
    print(words[i])