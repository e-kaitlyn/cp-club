import random
def bingo():
    b,i,n,g,o=[],[],[],[],[]
    ranges = [1,16,31,46,61,15,30,45,60,75]
    nums = [random.randint(1,15)]
    for i in range(74):
        x = (i+1)//15
        nums.append(random.randint(ranges[x],ranges[x+5]))
    b = nums[:15]
    i = nums[15:30]
    n = nums[30:45]
    g = nums[45:60]
    o = nums[60:]
    print("B I  N  G  O")
    for x in range(15):
        print(b[x],i[x],n[x],g[x],o[x],"\n")
bingo()