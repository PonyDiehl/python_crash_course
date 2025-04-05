#guests = ['tom', 'lisa', 'billy']
#message = f"Hey, {guests[0]}, {guests[1]}, {guests[2]}, do you want to come to the dinner party?"
#print(message)

#guests = ['tom', 'lisa', 'billy']
#guests.append('jerry')
#message = f"Hey {guests[0]} can't make it, {guests[1]}, {guests[2]}, {guests[3]},do you want to come to the dinner party?"
#print(message)

#guests = ['tom', 'lisa', 'billy']
#guests.append('jerry')
#del guests[0]
#message = f"Hey, {guests[0]}, {guests[1]}, {guests[2]} do you want to come to the dinner party?"
#print(message)

#guests = ['tom','lisa','billy']
#guests.insert(0,'jerry')
#guests.insert(2,'josh')
#guests.append('chelsea')
#message1 = f"Hey, {guests[0]}, do you want to come to the dinner party?"
#message2 = f"Hey, {guests[1]}, do you want to come to the dinner party?"
#message3 = f"Hey, {guests[2]}, do you want to come to the dinner party?"
#message4 = f"Hey, {guests[3]}, do you want to come to the dinner party?"
#message5 = f"Hey, {guests[4]}, do you want to come to the dinner party?"
#message6 = f"Hey, {guests[5]}, do you want to come to the dinner party?"
#print(message1, message2, message3, message4, message5, message6)

guests = ['tom','lisa','billy']
guests.insert(0,'jerry')
guests.insert(2,'josh')
guests.append('chelsea')

unenvited = guests.pop(0)
unenvited2 = guests.pop(1)
unenvited3 = guests.pop(2)
unenvited4 = guests.pop(-1)

print (f' Sorry, {unenvited.title()}, {unenvited2.title()}, {unenvited3.title()}, {unenvited4.title()}, there is only room for two at the table now, maybe next time')

message1 = f"Hey, {guests[0]}, do you want to come to the dinner party?"
message2 = f"Hey, {guests[1]}, do you want to come to the dinner party?"

print(message1, message2)