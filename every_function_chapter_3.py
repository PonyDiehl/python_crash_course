things = ["phone", "laptop", "tablet", "camera", "watch"]
people = ["Alice", "David", "Zach", "Bob", "Eve"]
places = ["mountain", "beach", "forest", "desert", "city"]

message = f'Hi {people[0].title ()}, I do you want to go the the {places[1]} with me today? Be sure to bring your {things[3]} with you!'
print (message)

people.append("Frank")

message2 = f'If {people} want to go as well feel free to invite them!'
print(message2)

message3 = f'I know {people[4]} is more of a city person, but I think they would enjoy it too, we are going to go to the {places[0]} after dinner.'
print(message3)