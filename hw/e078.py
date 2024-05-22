q = int(input())
result = []
while q!=0:
    r=q%2
    result.insert(0,str(r))
    q=q//2

print("".join(result))