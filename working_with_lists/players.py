# Slicing a list 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # First three players
print(players[1:4])  # Middle three players
print(players[:4]) # If the first index is omitted, it defaults to the beginning of the list
print(players[2:]) # If the last index is omitted, it defaults to the end of the list
print (players[-3:]) # Last three players

# Looping through a slice

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())