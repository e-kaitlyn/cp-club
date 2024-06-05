def triangle(a,b,c):
    if a>=b+c or b>=a+c or c>=a+b:
        return(False)
    else:
        return(True)

a,b,c= input().split()
print(triangle(int(a), int(b), int(c)))