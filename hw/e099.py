currentbase, convertbase = input().split()
currentbase, convertbase = int(currentbase), int(convertbase)
number = input()
if currentbase<2 or currentbase>16:
    print("error")
    exit()
if convertbase<2 or convertbase>16:
    print("error")
    exit()

def toTen(base, number):
    numTen = 0
    for i in range(len(number)):
        numTen += int(number[-(i+1)])*(base**(i))
    return(numTen)

def toBase(base, numTen):
    remainder = 0
    numBase = []
    while remainder<base:
        remainder = numTen%base
        numBase.insert(0,str(remainder))
        numTen = numTen//base
    numBase = "".join(numBase)
    return(numBase)


numTen = toTen(currentbase, number)
if convertbase == 10:
    print(numTen)
else:
    numBase = toBase(convertbase, numTen)
    print(numBase)


