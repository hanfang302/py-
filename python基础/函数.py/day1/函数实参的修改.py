def numberOne(a):
    a[0] = a[0]+1
    return a
b = [2]
print(numberOne(b))
print(b)

print('*'*50)

def numberTow(a,c):
    a.append(c)
    return a
d = [5]
print(numberTow(d,6))
print(d)

print('*'*50)

def number3(e):
    e['addres']='瑞士'

f = {'bieming':'世界屋脊','addres':'瑞士'}
print(f)

print('*'*50)
