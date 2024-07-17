def sublists(lst):
    n = len(lst)
    sublists = ["[]"]
     
    for s in range(n):
        for e in range(s + 1, n + 1):
            sublists.append(lst[s:e])
     
    return sublists
l = input().split()
print(sublists(l))