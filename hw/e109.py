number = int(input())
divisors=[]
for i in range(number):
    if i!=0:
        if number%i ==0:
            divisors.append(i)
    else:
        pass
print(divisors)