#Sorting a list permanently with .sort() method
# The .sort() method sorts the list in alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# .sort(reverse=True) will sort the list in reverse alphabetical order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with the sorted() function

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print ("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Reversing the order of a list with the reverse() method

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

print("\nHere is the reversed list:")
cars.reverse()
print(cars)

# Finding the length of a list with the len() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

