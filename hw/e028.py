t,v = input("air temp in c and wind speed in km/hr").split()
t,v = int(t), int(v)
wci = 13.12+0.6215(t)-11.27(v**0.16)+0.3965(t)(v**0.16)
print(wci)