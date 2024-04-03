ft,inch = input().split()
ft,inch = float(ft),float(inch)
inch+=(ft*12)
inch*=2.54
print(inch, "centimeters")