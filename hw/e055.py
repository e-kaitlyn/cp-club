radiation = input("Electromagnetic radiation (a x 10^b)").split()

a = int(radiation[0])
ab=radiation[2]
b=int(ab[3:])

if b<=9:
    if a<3:print("radio waves")
    else:print("microwaves")
elif b<12:print("microwaves")
elif b ==12:
    if a<3:print("microwaves")
    else:print("infrared light")
elif b <14:print("infrared light")
elif b==14:
    if a<4.3:print("infrared light")
    elif a<7.5: print("visible light")
    else:print("ultraviolet light")
elif b<17:print("x-rays")
elif b ==17:
    if a<3:print("ultraviolet light")
    else:print("x-rays")
elif b<19:print("x-rays")
elif b ==19:
    if a <3:print("x-rays")
    else:print("gamma rays")
else:print("gamma rays")