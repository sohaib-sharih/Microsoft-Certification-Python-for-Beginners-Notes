a = 22
b = 30
if a > b:
    print(a)
print(f"{a} this line is not indented.")

if a >= b:
    print(a)
else:
    print("not true")

if a > b:
    print("this is true")
elif a == b:
    print("this elif condition was found true.")
else:
    print("nothing was found to be true.")


d = 10
e = 20
f = 40

if d > e:
    if e < f:
        print("d is less than e AND e is less than f")
    else:
        print("d is less than F BUT not less than f")
elif e > f:
    print("not true, e is less than f")
else:
    print("so the previous condition was False")

# Add code below
object_size = 10
proximity = 9000

if object_size > 5 or proximity < 1000:
    print("Evasive maneuvers required.")
else:
    print("Object poses no threat")
