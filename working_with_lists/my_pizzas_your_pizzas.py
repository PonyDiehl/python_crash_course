pizzas =['meat lovers', 'hawaiian', 'buffalo chicken', 'supreme']
friends_pizzas = pizzas[:]
friends_pizzas.append('vegetarian')
for my_pizza in pizzas:
    print(my_pizza)
for friend_pizza in friends_pizzas:
    print(friend_pizza)
    print(f"My firend likes {friend_pizza} and a kambucha!\n")
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza} pizza and a pint!\n")
message = f"The best pizza is {pizzas[1].title()}!"
print(message)