db = int(input())
if db<40:
    print("less than a quiet room")
elif db==40:
    print("quiet room")
elif db<70:
    print("between quiet room and alarm clock")
elif db ==70:
    print("alarm clock")
elif db<106:
    print("between alarm clock and gas lawnmower")
elif db == 106:
    print("gas lawnmower")
elif db <130:
    print("between gas lawnmower and jackhammer")
elif db ==130:
    print("jackhammer")
elif db>130:
    print("more than a jackhammer")