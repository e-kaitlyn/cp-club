month,day = input().split()
day = int(day)
if month == "january":
    if day>19:print("aquarius")
    else:print("capricorn")
elif month == "feburary":
    if day>18:print("pisces")
    else:print("aquarius")
elif month == "march":
    if day>20:print("aries")
    else:print("pisces")
elif month == "april":
    if day>19:print("taurus")
    else:print("aries")
elif month == "may":
    if day>20:print("gemini")
    else:print("taurus")
elif month == "june":
    if day>20:print("cancer")
    else:print("gemini")
elif month == "july":
    if day>22:
        print("leo")
    else: print("cancer")
elif month == "august":
    if day>22:print("virgo")
    else: print("leo")
elif month == "september":
    if day>22:print("libra")
    else:print("virgo")
elif month == "october":
    if day>22:print("scorpio")
    else:print("libra")
elif month == "november":
    if day>21:print("sagittarius")
    else:print("scorpio")
elif month == "december":
    if day>21:print("capricorn")
    else:print("sagittarius")