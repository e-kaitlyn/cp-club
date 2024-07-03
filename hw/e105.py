n = int(input())
numbers = []
newnumber = []
while n!=0:
    numbers.append(n)
    n = int(input())
if len(numbers)<=4:
    print("Need more than 4 numbers")
    exit()

newnumber=sorted(numbers)
del newnumber[0]
del newnumber[-1]
print(numbers)
print(newnumber)
