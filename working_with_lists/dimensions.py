# Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple
for dimesion in dimensions:
    print(dimesion)

# Writing Over a Tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)