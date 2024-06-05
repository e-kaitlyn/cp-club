import random
def flip():
    if random.randint(1,2) == 1:
        return("H")
    else:
        return("T")
total=0
for i in range(10):
    line = []
    count = 1
    output = ()
    while line[-3:]!="H" or line[-3:]!="T" or len(line)<3:
        flips =()
        line.append(flip())
    
    t = int(len(line))
    flips = "("+str(t) + " flips)"
    line.append(flips)
    print(' '.join(line))
    total+=t
avg = total/10
print("On average,",avg,"flips were needed")