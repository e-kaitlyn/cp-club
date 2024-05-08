yr = int(input())
mth = int(input())
day = int(input())

if day != 30 or day != 31:
    if mth != 2 and day != 28:
        print(yr,mth,(day+1))
    elif yr % 400 == 0:
            print(yr,"2 29")
        if yr % 100 != 0 and yr % 4 == 0:
            print(yr, "2 29")
        else:
            print(yr,"3 1")
elif mth in [1,3,5,7,8,10,12]:
    if day == 30:
        print(yr,mth,"31")
    elif mth!=12:
        print(yr,(mth+1),"1")
    else:
        print((yr+1),"1 1")
else:
    print(yr,(mth+1),"1")