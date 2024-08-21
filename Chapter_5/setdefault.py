spam = {'name': 'Pooka', 'age': 5}
if 'color1' not in spam:
    spam['color1'] = 'black'

print(spam)

#Optimization
spam.setdefault('color2', 'black')
print(spam)

# Return the value if its already set
print(spam.setdefault('color1', 'white'))
