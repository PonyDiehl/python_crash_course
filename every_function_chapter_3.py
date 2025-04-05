things = ["phone", "laptop", "tablet", "camera", "watch"]
people = ["Alice", "David", "Zach", "Bob", "Eve"]
places = ["mountain", "beach", "forest", "desert", "city"]

message = f'Hi {people[0].title ()}, I do you want to go the the {places[1]} with me today? Be sure to bring your {things[3]} with you!'
print (message)

people.append("Frank")

message2 = f'If {people[1], people[2], people[3], people[4], people[5]} want to go as well feel free to invite them!'
print(message2)

message3 = f'I know {people[4]} is more of a city person, but I think they would enjoy it too, we are going to go to the {places[0]} after dinner.'
print(message3)

things.sort()
message4 = f'I am going to bring all my {things} with me in case anyone needs to use them'
print(message4)

places.sort(reverse=True)
places.pop(0)
places.pop(1)
message5 = f'Next time we can go to the {places}!'
print(message5)