magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your nxt trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!\n")
print(f"Up next we have {magicians[0].title()} taking the stage!")