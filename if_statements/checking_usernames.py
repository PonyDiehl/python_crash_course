current_users = ['mike', 'sarah', 'kim', 'tom','beath']
new_users = ['kelly','jim','dug','sean','kim']

for new_users in new_users:
    if new_users in current_users:
        print(f"User {current_users} name is not avalible")
    else:
        print(f'User name {new_users} avalible')
