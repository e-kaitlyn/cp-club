def isPrime (number) :
    if number > 1: 
        for x in range (2, number) :
            if number % x == 0:
                return False
        return True
    else:
        return False

def nextprime(n):
    x=n//6
    if (6*x+1)<=n:
        x+=1
    if isPrime(6*x+1):
        return(6*x+1)
    else:
        if (6*x-1)<=n:
            x+=1
        return(6*x-1)
    

n = int(input("enter a number"))
print(nextprime(n))