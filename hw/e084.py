a,b,c = (input().split())
num = [int(a),int(b),int(c)]
num.remove(min(num))
num.remove(max(num))
print(num[0])