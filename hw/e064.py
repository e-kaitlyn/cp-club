t = ""
rt =""
tenth = ""
value=0
while True:
    a= (input("enter amounts"))
    if a == '':
        break
    value +=float(a)

rt= str(value)
t=str(value)
tenth = t[-2]
if t[-1] == "0" or t[-1]=="5":
    print(t)
    print(rt)
elif t[-1] == "1" or t[-1] == "2":
    rt[-1] = "0"
    print(t)
    print(rt)
elif t[-1] == "3" or t[-1] == "4" or t[-1] == "6" or t[-1] == "7":
    rt[-1] = "5"
    print(t)
    print(rt)
else:
    tenth = str(int(tenth)+1)
    rt[-1] = "0"
    rt[-2] = tenth
    print(t)
    print(rt)
