n = int(input())
numbers = []
while n!=0:
    numbers.append(n)
    n = int(input())
numbers.sort()
for i in range(len(numbers)):
    print(numbers[-(i+1)])