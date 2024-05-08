wave=int(input())
if wave<380:
    print("not in spectrum")
elif wave<450:
    print("violet")
elif wave<495:
    print("blue")
elif wave<570:
    print("green")
elif wave<590:
    print("yellow")
elif wave<620:
    print("orange")
elif wave<=750:
    print("red")
else:
    print("not in spectrum")