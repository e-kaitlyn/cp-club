import math
s,n = map(int,input().split())
#s,n = int(s), int(n)

a = (n*s**2)/(4*math.tan(math.pi/n))
print(round(a,2))