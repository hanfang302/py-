def modify(v):
    v[0] = v[0]+1
    return v 

a = [2]
print(modify(a))
print(a)

print('*'*45)

def modify2(v,item):
    v.append(item)
    return v

b = [4]
print(modify2(b,5))
print(b)
print('*'*45)

def modify3(c):
    c['age']=20
d = {'name':'张三','age':'20'}
print(d)

