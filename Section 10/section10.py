def partsA():
    print("sohaib")

partsB = partsA()

print(partsB)

# When a function does not return a value explicitly, then it returns NONE, to have a value in return, you need to implicitly return a value.

def partsC():
    return 5 + 5

partsD = partsC()
print(partsD) 
'''returns 10'''
any([True, False])
print(any(['sohaib', False]))

# function with arguments

def moonDist(moonD):
    print(f"the distance of the moon is: {moonD}")

moonDist(222)

def sunDict(sunD):
    if sunD == 200:
        print(f"The distance of the sun is: {sunD}")
    else:
        print("Not valid")

sunDict(4000)
sunDict(200)
# sunDict()will give a type error

def speedLight(speed, time):
    distance = speed * time
    print(f" the distance travelled will be:{distance}")

speedLight(100, 3.5)

# using keyword arguments and multiple arugments in a function of datetime

from datetime import timedelta, datetime

def distMoon(destination, hours=33):
    now = datetime.now()
    print(f"Current time is: {now}")
    arrival = now + timedelta(hours=hours)
    print(f"{arrival} is the time taken for Arrival: %H:%M")
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

distMoon("Earth",hours=250)

# Variable arguments

def speedSun(*args):
    for key in args:
        print(f"This is the best {key} dish ive had")


speedSun("cake",'biryani',100)

# Keyword Arguments

def carSpeed(**kwargs):
    for key in kwargs.values():
        print(f"This is the best car of this year: {key}")

carSpeed(car="Ferrari",NextCar='Toyota',lastCar='honda accord',bestcar=1000)
