num = input()
nums = []
negative = []
zero = []
positive = []
sort = []
while num != "":
    nums.append(int(num))
    num = input()

for i in range(len(nums)):
    if nums[i]<0:
        negative.append(nums[i])
    elif nums[i]==0:
        zero.append(nums[i])
    else:
        positive.append(nums[i])

sort.append(negative)
sort.append(zero)
sort.append(positive)
for i in range(len(sort)):
    print(sort[i])