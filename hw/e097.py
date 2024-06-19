import random
def randompass():
    password = ""
    for i in range(random.randint(7,10)):
        password+=(chr(random.randint(33,126)))
    return(password)
upper = ["A","B","C","D","E",'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ["0",'1','2','3','4','5','6','7','8','9']
def check(password):
    if len(password)>=8:
        if any(i in password for i in upper):
            if any(i in password for i in lower):
                if any(i in password for i in number):
                    return(True)
                    exit
    return(False)


count = 0
while True:
    password = randompass()
    if check(password) == True:
        print(password)
        print(count)
        break
    else:
        count+=1