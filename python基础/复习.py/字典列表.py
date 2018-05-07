#a1 = {'color': 'green', 'points': 5}
#a2 = {'color': 'yellow', 'points': 10}
#a3 = {'color': 'red', 'points': 15}
#a = [a1,a2,a3]
#for ab in a:
    #print(ab)

a = []
for a_number in range(30):
    new_a = {'color': 'green', 'points': 5, 'speed': 'slow'}
    a.append(new_a)
for ab in a[:5]:
    print(ab)
print('-'*50)
print(str(len(a)))
