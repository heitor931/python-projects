# Consider the following 2 Lists: names = ["Dan", "John", "Diana"] and phones = [11111, 2222, 3333].

names = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]

result = set([(m,phones[n]) for n,m in enumerate(names)])

zipped = set(zip(names,phones))
print(zipped)