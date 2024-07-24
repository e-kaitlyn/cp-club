import random
def roll():
    return(random.randint(1,6)+random.randint(1,6))
def percent(x):
    percent = x/10
    return(percent)
two = three = four = five = six = seven = eight = nine = ten = eleven = twelve = 0
for i in range(1000):
    dice = roll()
    if dice<6:
        if dice == 2: two+=1
        if dice == 3: three +=1
        if dice == 4: four+=1
        if dice == 5: five+=1
    if dice>6:
        if dice == 7: seven+=1
        if dice == 8: eight+=1
        if dice == 9: nine+=1
        if dice == 10: ten+=1
        if dice == 11: eleven +=1
        if dice == 12: twelve +=1
    else: six +=1
import pandas as pd

data = {'total':[2,3,4,5,6,7,8,9,10,11,12],
        'simulated percent':  [percent(two),percent(three),percent(four),percent(five),percent(six),percent(seven),percent(eight),percent(nine),percent(ten),percent(eleven),percent(twelve)],
        'expected percent': ['2.78','5.56','8.33','11.11','13.89','16.67','13.89','11.11','8.33','5.56','2.78'],
        }

df = pd.DataFrame(data)

print(df)

