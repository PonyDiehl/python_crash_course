current_users = ['mike', 'sarah', 'kim', 'tom','beath']
new_users = ['kelly','jim','dug','sean','kim']

for new_users in current_users:
    if new_users in current_users:
        print(f"User name {current_users} is not avalible")
