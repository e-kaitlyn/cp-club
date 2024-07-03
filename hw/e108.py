num = input()
nums = []
while num != "":
    nums.append(int(num))
    num = input()
nums.sort()
for i in range(len(nums)):
    print(nums[i])