def perfect(num):
    divisors = []
    for i in range(num):
        if i != 0:
            if num % i == 0:
                divisors.append(i)
        else:
            pass
    sum = 0
    for i in range(len(divisors)):
        sum +=divisors[i]
    if sum == num:
        return(True)
    else:
        return(False)
perfects = []
for i in range(10000):
    if perfect(i):
        perfects.append(i)
print(perfects)