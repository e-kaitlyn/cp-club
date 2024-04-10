import math
ra, he = input().split()

base = math.pi*(int(ra)**2)
volume = round(base*int(he), 1)
print(volume)