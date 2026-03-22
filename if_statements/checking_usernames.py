current_users = ['Mike', 'Sarah', 'Kim', 'Tom', 'Beath']
current_users = ['mike', 'sarah', 'kim', 'tom','beath']
new_users = ['kelly','jim','dug','sean','kim']

for new_user in new_users:
    if new_user in current_users:
        print(f"Username {new_user.title()} is not avalible, enter new user name.")
    else:
        print(f'Username {new_user.title()} avalible.')
