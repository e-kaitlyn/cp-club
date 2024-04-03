c = int(input())
two = c//200
c = c%200
one = c//100
c = c%100
qua = c//25
c = c%25
dim = c//10
c = c%10
nic = c//5
c = c%5
print(two, "toonies,", one, "loonies,", qua, "quaters,",dim,"dimes,",nic,"nickles,",c,"pennies")