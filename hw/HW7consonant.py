#Iterative
def consonant(string):
    vowels = "aeiouAEIOU"
    count = 0

    for i in string:
        if i not in vowels and i.isalpha():
            count +=1
    return count

string = input()
print(consonant(string))

#rescrusive
