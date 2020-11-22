# lists
heroes = ['Iron man', 'superman', 'batman']
# square brackets are used for lists
mixed = [2, "list", 3.50]
# we can mix several data types
# and lists are mutable
heroes.append('Captain America')
print(heroes)
# in the output, the last element is Captain America

# enumerate() function with list of tuples
people = [('Susan', 59), ('Mary', 30), ('Steven', 78)]
for idx, (name, mark) in enumerate(people):
    print("index is", idx, "name is", name, "and mark is", mark)

# another example of enumerate function
names = ['Steven', 'Mary', 'Susan']
for i, item in enumerate(names):
    print(i, item)
