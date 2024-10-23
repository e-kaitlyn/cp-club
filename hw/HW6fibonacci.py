def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
def sequence(n):
    sequence = []
    for i in range(n):
        sequence.append(fib(i))
    return sequence

n = int(input())
print(sequence(n))