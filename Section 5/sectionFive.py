fat = "sohaib Sharih"
fatTwo = fat + "thanks Allah for everything."
print(fatTwo)

fatThree = fatTwo + """And he is striving improve both the live's of the poeple and himself, "isn't it?", yes : 44 C"""
print(fatThree)
print(f"this is a list converted: ${fatThree.split()}")

print(fatThree.find("the"))
print(fatThree.count("the"))

# Using IN to find a string within a string statement
inA = "Moon" in "Moon is an essential part of earth."
print(f"using IN: {inA}")

# To use index to find a string word in a sentence using split method
fatThree.split(':')
fatNew = fatThree.split(':')
print(f"this is the fatNew value:{fatNew}")
print(fatNew[-1])

# if you use the split method directly without storing the list inside a variable, then it will only split it but not store it inside a variable, and following code that prints the index, will print the index of the character from the string instead of a 
print(f"This is fatThree: {fatThree.split(':')}")
print(fatThree[0])
print(fatThree[-1])

# for loops

goodA = "There is only one best place in the world, that is the country number 3"

for item in goodA.split():
    if item.isnumeric():
        print(f"print the item value: {item}")

if "this is Sohaib".endswith("Sohaib"):
    print("it really ends with Sohaib")

if "start with".startswith("s"):
    print("yes ends with S")

#  using join method after split method was used.
    
goodB = "This is an item from mars"
goodBsplit = goodB.split()
print(goodBsplit)
print(' '.join(goodBsplit))

#  using %s
goodC = 12
print("this is the best %s years of my life!!!" % goodC)

# replace method
goodD = "this is the best year of my life"
print(goodD.replace('life','200'))

#  using the join Method

boxJ = ["sohaib", "sharih", "Pakistani"]
print('--'.join(boxJ))

# using an expression of f string doesn't require a function call
bfA = "sohaib sharih"
bfaB = f"{bfA.title()}"
print(bfaB)

print(f"this is the best angle: {round(5/199, 2)}")