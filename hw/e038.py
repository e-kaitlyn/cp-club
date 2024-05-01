zero= ["april", "june","september","november"]
month = input()
if month in zero:
    print("30")
elif month == "february":
    print("28 or 29")
else:
    print("31")
