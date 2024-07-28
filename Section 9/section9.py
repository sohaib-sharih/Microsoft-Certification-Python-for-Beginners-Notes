names = {
    'name':'sohaib sharih',
    'age': 38
}
print(names)
print(names.get('age'))
"""the below print function call will give an output of NONE"""
print(names.get('model')) 
# print(names.get['model'])  this will give an error
print(names['age'])
listA = ['sohaib','sharih','salman','fahad']
print(listA[0])
print(listA)

names.update({'name':'Fahad HAmid'})
print(names)

names['model'] = 1999
names.update({
    'country':'Pakistan',
    'City': 'Karachi'
})
print(names)

names.pop('City')
print(names)

# Nested Dictionary
names['country'] = ({
    'car':'Honda Accord'
})

print(names)

# retreiving nested dictionary

print(f"this is the {names.get('name')} and the nested value is: {names['country']['car']}")

nameKeys = names.keys()
print(nameKeys)

# values only
nameValues = names.values()
print(nameValues)

# getting all keys using for loop to print the values of the keys.
for key in names.keys():
    print(f"{key}:{names[key]}")


# determine if a key exists:
if 'age' in names:
    names['age']= names['age'] + 222
    print(names['age'])
        
else:
    print(f"This is {names['age']}")

# To retrieve all values
    
for value in names.values():
    print(value)