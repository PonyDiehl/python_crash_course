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

# Checking for special items 

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")

print('\nFinished making your pizza!')
