import random

def bingo():
    bingo = {}
    ranges = [1,16,31,46,61,15,30,45,60,75]
    nums = [random.randint(1,15)]
    for i in range(24):
        x = (i+1)//5
        nums.append(random.randint(ranges[x],ranges[x+5]))
    bingo['B'] = nums[:5]
    bingo['I'] = nums[5:10]
    bingo['N'] = nums[10:15]
    bingo['G'] = nums[15:20]
    bingo['O'] = nums[20:]
    return bingo
card = bingo()
keys = ['B','I','N','G','O']
for k in card:
    print(f"   {k} ",end="")
print()
for i in range(5):
    for letter in keys:
        print("%4d " % card[letter][i], end="")
    print()