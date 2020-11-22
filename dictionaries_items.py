# dictionaries
WIUT = {'BIS': ('FunPro', 'CSF'), 'Foundation': ('QM', 'Academic English')}
# curly brackets are used for dictionaries with key-value pairs
# accessing values of dicts
print(WIUT['BIS'])
# adding elements
WIUT['BM'] = 'Intro to Management'
print(WIUT)

# the use of items() method
print(WIUT.items())
# output is list of tuples
# dict_items([('BIS', ('FunPro', 'CSF')), ('Foundation', ('QM', 'Academic English')), ('BM', 'Intro to Management')])
print(list(WIUT.items()))
