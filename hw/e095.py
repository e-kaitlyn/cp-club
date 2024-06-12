import random
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def license():
    plate=[]

    if random.randint(1,2) ==1:
        for i in range(3):
            plate.append(letters[random.randint(0, 25)])
        for i in range(3):
            plate.append(str(random.randint(0,9)))
    else:
        for i in range(4):
            plate.append(str(random.randint(0, 9)))
        for i in range(3):
            plate.append(letters[random.randint(0, 25)])
    return("".join(plate))

print(license())