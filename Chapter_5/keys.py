spam = {'color': 'red', 'age': 42}

print("*****Print values**** dictionary.values()")
print(type(spam.values()))
for v in spam.values():
    print(v)
print(type(list(spam.values())))

print("*****Print keys***** dictionary.keys()")
print(type(spam.keys()))
for v in spam.keys():
    print(v)
print(type(list(spam.values())))

print("*****Print items***** dictionary.items()")
print(type(spam.items()))
for v in spam.items():
    print(v)
print(type(list(spam.values())))


