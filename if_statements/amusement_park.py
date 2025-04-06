# if elif else statements
age = 12
if age < 4:
    print("it's free")
elif age < 18:
    print("it's $25 for you")
else:
    print("it's $50 for you")
# Using {price} variable after the statement instead of print 
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 50
print(f"Your ticket price is ${price}")
# Using multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 50
else: 
    price = 30
print(f"Your ticket price is ${price}")
# Ommitting the else statement
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 50
elif age >= 65:
    price = 30
print(f"Your ticket price is ${price}")