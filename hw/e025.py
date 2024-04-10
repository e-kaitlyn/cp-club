s = int(input())
d = s//86400
s = s%86400
h = s//3600
s = s%3600
m = s//60
s = s%60

if h<10:
    h = str(h)
    h = h.zfill(2)

if m<10:
    m = str(m)
    m = m.zfill(2)

if s<10:
    s = str(s)
    s = s.zfill(2)
print(f'{d}:{h}:{m}:{s}')
















