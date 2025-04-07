current_users = ['mike', 'sarah', 'kim', 'tom','beath']
new_users = ['kelly','jim','dug','sean','kim']

for new_user in new_users:
    if new_user in current_users:
        print(f"User {new_user} name is not avalible, enter new user name")
    else:
        print(f'User name {new_user} avalible')
