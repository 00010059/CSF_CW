# tuples
heroes = ('Superman', 'Batman', 'Spider-Man', 'Batman')
# round brackets are used for tuples
mixed = (2, "list", 3.50)
# we can mix data types in tuples too
# tuples are immutable
# this is how indexing works
print("the index of Batman is ",heroes.index('Batman'))
# slicing in tuples
print(heroes[1:3])
# counting the elements
print(heroes.count('Batman'))
# it is possible to use list of tuples

# we can concatenate two sequences with zip function
name = ('hat', 'jacket', 'sneekers')
price = (6, 20, 32)
zippd = zip(name,price)
for (a, b) in zippd:
    print(a, "$",b)

# or in a form of list of tuples
zippd = list(zip(name, price))
print(zippd)
