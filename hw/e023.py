import math
s,n = input().split()
s,n = int(s), int(n)

a = (n*s**2)/(4*math.tan(math.pi/n))
print(round(a,2))