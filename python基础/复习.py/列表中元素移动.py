user = ['a','b','c']
users = []
while user:
    user_name = user.pop()
    print('verifying user:' +' '+ user_name.title())
    users.append(user_name)

print('\nThe following users have been confirned:')
for user1 in users:
    print(user1.title())


pets = ['dog','cat','dog','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
