def lmc(m,n):
    d = min(m,n)
    while m%d!=0 or n%d!=0:
        d-=1
    return(d)
def fraction(n,d):
    divisor = lmc(n,d)
    n=n/divisor
    d=d/divisor
    return(int(n),int(d))

n=int(input("numerator"))
d=int(input("denominator"))
print(fraction(n,d))