#guests = ['tom', 'lisa', 'billy']
#message = f"Hey, {guests[0]}, {guests[1]}, {guests[2]}, do you want to come to the dinner party?"
#print(message)

guests = ['tom', 'lisa', 'billy']
guests.append('jerry')
del guests[0]
message = f"Hey, {guests[0]}, {guests[1]}, {guests[2]} do you want to come to the dinner party?"

print(message)