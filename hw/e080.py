import random
def flip():
    if random.randint(1,2) == 1:
        return("H")
    else:
        return("T")
i=0
total=0
t=0
while i<10:
    line = []
    count = 1
    output = ()
    while count<3:
        flips =()
        line.append(flip())
        if line[-1] == output or len(line)==0:
            count+=1
        else:
            output=line[-1]
            count =1
        t = int(len(line))
        flips = "("+str(t) + " flips)"
    line.append(flips)
    print(' '.join(line))
    total+=t
    i+=1
avg = total/10
print("On average,",avg,"flips were needed")