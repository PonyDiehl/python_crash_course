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
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print("\nFinished maiking your pizza")