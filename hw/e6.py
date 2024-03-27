money = int(input("how much money spend"))
tip = int((money*100)*0.18)
tip = float(tip/100)

tax = int((money*100)*1.13)
tax = float(tax/100)

print("tax:", tax,"tip:", tip, "total:", (tax+tip+money))