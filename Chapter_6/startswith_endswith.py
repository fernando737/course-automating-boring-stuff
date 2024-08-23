print(r"Hello, world!'.startswith('Hello')")
print('Hello, world!'.startswith('Hello')) #True
print(r"Hello, world!'.startswith('Hello')")
print('Hello, world!'.endswith('world!')) #True
print(r"'abc123'.startswith('abcdef')")
print('abc123'.startswith('abcdef')) #False
print(r"'abc123'.endswith('12')")
print('abc123'.endswith('12')) #False
print(r"'Hello, world!'.startswith('Hello, world!')")
print('Hello, world!'.startswith('Hello, world!')) #True
print(r"'Hello, world!'.endswith('Hello, world!')")
print('Hello, world!'.endswith('Hello, world!')) #True