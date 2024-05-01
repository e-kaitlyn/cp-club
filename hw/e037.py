shapes=["triangle","quadrilateral","pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon"]
sides = int(input())
sides-=3
if sides<0 or sides>7:
    print("error")
else:
    print(shapes[sides])
