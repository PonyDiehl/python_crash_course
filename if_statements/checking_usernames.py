new_users = 'kim'

current_users = ['mike', 'sarah', 'kim', 'tom','beath']
new_users = ['kelly','jim','dug','sean','kim']

for new_user in new_users:
    if new_user in current_users:
        print(f"User {current_users} name is not avalible")
    else:
        print(f'User name {new_users} avalible')
