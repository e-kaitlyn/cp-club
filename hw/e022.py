import math
s1, s2, s3 = map(int,input().split())
#s1,s2,s3 = int(s1), int(s2), int(s3)
s = (s1+s2+s3)/2
a = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(a)