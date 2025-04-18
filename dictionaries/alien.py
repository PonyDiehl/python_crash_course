# Sample dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Accessing values in a dictionary 

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding new key-value pairs

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary 

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying values in a dictionary 

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

# Tracking the position of the alien 

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Orignal position: {alien_0['x_position']}")

# Move the alien to the right 
# Determine how far to move the alien based on its current speed 

if alien_0 ['speed'] == 'slow':
    x_increment = 1
elif alien_0 ['speed'] == 'medium':
    x_increment = 2
else:
    # Fast alien
    x_increment = 3
# The new position is the orignal position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position {alien_0['x_position']}")

# Removing key-value pairs 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Using get() to access values

alien_0 = {'color': 'green', 'speed':'slow',}
point_value = alien_0.get('points', ' No point value assigned.')

print(point_value)