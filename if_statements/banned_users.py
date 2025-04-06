# Checking wheather a value is not in a list 

banned_users = ['andrew', 'tim', 'sam']
user = 'marie'

if user not in banned_users:
    print(f'Welcome, to the party {user.title()}!')
else:
    print(f'Sorry, you are banned {user.title()}, go home!')