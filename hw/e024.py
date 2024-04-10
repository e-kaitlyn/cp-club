d, h , m, s = input().split()
d,h,m,s = int(d), int(h), int(m), int(s)
h +=d*24
m += h*60
s += m *60
print(s)