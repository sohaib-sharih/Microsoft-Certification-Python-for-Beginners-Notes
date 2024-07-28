planets = ['mars','earth','neptune']
planets[0] = 'house'
print(planets)
# number of items in a list

print(len(planets))
newPlanets = planets.append('sun')
print(planets)

print(planets.pop())
removePlanets = planets.pop()
print(f"the item removed from {planets} is the following {removePlanets}")

# min and max()

numbersA = [1, 4, 3, 5, 6]
print(min(numbersA))
print(max(numbersA))

# using slice
sliceA = [1, 33, 44, 555, 6644, 22]
print(sliceA[0:2])
# joining
newList = planets + sliceA
print(newList)
# sorting
print(sliceA)
sliceA.sort()
print(sliceA)
sliceA.sort(reverse=True)
print(sliceA)
