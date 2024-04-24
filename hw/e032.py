num=[]
a,b,c = map(int,input().split())
num.extend([a,b,c])
s = min(num)
num.remove(s)
m = min(num)
num.remove(m)
l = num[0]
print(s,m,l)