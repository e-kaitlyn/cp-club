s = input()
p = True
if len(s) % 2 == 0:
    count = len(s) / 2
else:
    count = (len(s)-1)/2

for i in range(int(count)):
    if s[i] == s[-(i+1)]:
        p = True
    else:
        p = False
        break

if p == True:
    print('yes')
else:
    print("no")