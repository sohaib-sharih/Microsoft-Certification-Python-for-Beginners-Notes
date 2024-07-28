# while loops to take user input
user_input = ''
inputs = []
while user_input.lower() != 'done':
    print(f"User input is {user_input}")
    user_input = input("Enter a value, to stop enter 'done' only")
    if user_input:
        inputs.append(user_input)
        print(inputs)

# for loop
from time import sleep  
countDown = ['sohaib','sharih','loop','jacket']
for item in countDown:
    print(item)
    sleep(1)
print("blast offA")
    