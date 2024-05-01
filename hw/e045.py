cord = input()
letter = cord[0]
number = (int(cord[1]))-1
colour = 0
if letter in ["a","c","e","g"]:
    colour+=1
colour+=(number)
if colour%2 == 0:
    print("white")
else:
    print("black")