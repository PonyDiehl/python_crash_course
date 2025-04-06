# Checking for Inequality. 
# Equality opperator is '=='
# Inequality opperator is '!='

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_topping = 'anchovies'
if requested_topping == 'anchovies':
    print("Gimme them fish!")
# Testing mutiple conditions 
# Using the if statement multiple times creates mutiple indipendent tests that will run regaurdless of if the test before it passes
# or fails.
# If you want only one block of code to run, use an (if-elif-else) chain. If more than one block of code needs to run, use a series 
# of indipendent (if) statements.
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print("\nFinished maiking your pizza")

# Checking for special items.

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")

print('\nFinished making your pizza!')

# Using if statements inside a loop.

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else: 
        print((f"Adding {requested_topping}."))
print(f"Finished making your pizza!")

# Cheching that a list is not empty.

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished maiking your pizza!")
else:
    print("Are you sure you want a plain pizza?")