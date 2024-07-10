num = input()
nums = []
below = []
avgs = []
above = []
while num != "":
    nums.append(int(num))
    num = input()
avg = 0
for i in range(len(nums)):
    avg+=nums[i]
avg= avg/len(nums)
for i in range(len(nums)):
    if nums[i]< avg:
        below.append(nums[i])
    elif nums[i] == avg:
        avgs.append(nums[i])
    else:
        above.append(nums[i])
print("Average of",avg)
print(below)
print(avgs)
print(above)