def largestSum(lis):
    if len(lis)<2:
        return -1
    
    max1 = 0
    max2 = 0
    for i in range(len(lis)):
        if lis[i] > max1:
            max2 = max1
            max1 = lis[i]
        elif lis[i] > max2:
            max2 = lis[i]
    return max1+max2

def largestSum2(lis):
    if len(lis)<2:
        return -1
    max1 = max(lis)
    lis.remove(max1)
    max2 = max(lis)

    return max1 + max2

print(largestSum2([12, 34, 10, 6, 40]))
print(largestSum2([10, 10, 10]))
print(largestSum2([10]))
