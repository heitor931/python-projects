d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

d2 = dict()
for el in sorted(d1.values()):
    for d,v in d1.items():
        if v == el:
            d2[d] = v

print(d2)

