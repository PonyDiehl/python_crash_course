world = ["Miami", "Brisbane", "Paris", "Tokyo", "New York", "London", "Berlin", "Madrid", "Rome", "Sydney"]
print(world)

# sorted() function sorts the list in alphabetical order but does not change the original list

print("\nHere is the sorted list:")
print(sorted(world))

# The original list remains unchanged

print(world)

print("\nHere is the sorted list in reverse order:")
print(sorted(world, reverse=True))

print(sorted(world, reverse=False))

# The sort() method sorts the list in alphabetical order and premarily changes the original list

print("\nHere is the 'sort()' list:")

world.sort()
print(world)