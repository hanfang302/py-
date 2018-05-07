number = 1
while number <= 5:
    print(number)
    number += 1

prompt = '\nTell me something,and i will repeat it back to you:'
prompt += '\nEnter "quit" to end the programi.'
message = ''
while message != 'quit':
    message = input(prompt)
   
    if message != 'quit':
        print(message)

prompt = '\nTell me something,and i will repeat it back to you:'
prompt += '\nEnter "quit" to end the programi.'
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = '\nTell me something,and i will repeat it back to you:'
prompt += '\nEnter "quit" to end the programi.'
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("'I'd love to go to: " + city.title() + '!')

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)

       
