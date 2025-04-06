# Equality operator, boolian expression
user = 'top rank'
if user == 'top rank':
    print('You are the top rank user')
# Inequality operator, boolian expression
user = 'not to rank'
if user != 'top rank':
    print('You are not the top rank user')
# Boolean expression using the lower() method
user = 'TOP RANK'
if user.lower() == 'top rank':
    print('You are the top rank user')
# Boolean expression using numeric values
user_age = 18
if user_age >= 18:
    print('You are an adult')
user_age = 17
if user_age != 18:
    print('You are not 18')
user_age = 17
if user_age < 18:
    print("You're still a kid")
user_age = 18
if user_age == 18:
    print("Now you can vote")
# Boolian experssions using the (and) operator and the (or) operator
user1_age = 18
user2_age = 17
if user1_age and user2_age >= 18:
    print('You are both adults')
else:
    print('You are not both adults')
user1_age = 18
user2_age = 17
if user1_age >= 18 or user2_age >= 18:
    print('At least one of you is an adult')
# Boolean expression testing wheather a value is in a list
registered_users = ['player1', 'player2', 'player3']
user = 'palyer4'
if user not in registered_users:
    print(f'{user.title()} Sign up to play!')
