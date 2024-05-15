cost = 0
while True:
    age= input()
    if age == "":
        break
    if int(age) <3:
        cost +=0
    elif int(age)>2 and int(age)<13:
        cost +=14.00
    elif int(age)>64:
        cost+=18.00
    else:
        cost +=23.00
print(cost)