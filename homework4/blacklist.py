casino_blacklist = {"John Dow", "Bella Goth", "Mortimer Goth", "Don Lotario"}
poker_blacklist = {"John Dow", "Dont Lotario", "Bella Goth"}
alcohol_blacklist = {"John Dow", "Malcolm Landgraab", "Bella Goth"}

common_blacklist = casino_blacklist & poker_blacklist & alcohol_blacklist

print("People on all blacklists:")
for person in common_blacklist:
    print(person)
