def anagram(s):
    d = {}
    x = 1
    for i in s:
        if i not in d:
            d[i]=x
        else:
            d[i]+=1
    return d
def check(s1,s2):
    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")
    s1 = s1.upper()
    s2 = s2.upper()
    if anagram(s1) == anagram(s2):
        return(s1+" and "+s2+" are anagrams")
    else:
        return(s1+" and "+s2+" are not anagrams")

s1 = input()
s2 = input()

print(check(s1,s2))