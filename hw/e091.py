op=["+","-","*","/","^"]
num = [1,1,2,2,3]
def precedence(operater):
    if operater in op:
        print(num[op.index(operater)])
    else:
        return("-1")
a = input()
print(precedence(a))