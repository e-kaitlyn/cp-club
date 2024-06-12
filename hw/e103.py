month,day,year = input("input date").split()
months = ["january","feburary","march","april","may","june","july","august","september","october","november","december"]
month = int(months.index(month))+1
day = int(day)
year = int(year[-2:])

def magic(month,day,year):
    if month*day == year:
        return(True)
    else:
        return(False)

print(magic(month,day,year))