line = input().split()
vowels = ["a","e","i","o","u","A","E","I","O","U"]
pigline =""
for i in range(len(line)):
    word = line[i]
    if word[0] in vowels:
        word+=("way")
    else:
        extra = ""
        for x in range(len(word)):
            if word[x] in vowels:
                word+=(extra)
                break
            else:
                extra+=word[x]
        word = word[len(extra):]
    if i!=0:
        pigline+=" "
    pigline+=(word)

print(pigline)