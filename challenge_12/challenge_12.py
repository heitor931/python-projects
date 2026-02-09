# Considering the following dict, get a dict representation sorted by key.

# A dict representation means viewing or printing the dict.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

d2 = dict()
for el in sorted(d1):
    for d,v in d1.items():
        if el == d:
            d2[el] = v

print(d2)