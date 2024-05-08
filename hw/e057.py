yr = int(input())
leap = False
if yr%400 == 0:
    leap = True
elif yr%100!=0 and yr%4==0:
    leap = True
print(leap)