def say(message,times=1):
    print((message+'')*times)


say.__defaults__
print('*'*45)

say('hello')
print('*'*45)
say('world\n',5)
