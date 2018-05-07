#a = [x for x in range(4)]
#print(a)
#b = [x for x in range(1,18)]
#print(b)
#c = [x for x in range(2,15,3)]
#print(c)
a = [(x,y) for x in range(1,4) for y in range(3)]
print(a)
print('-'*80)
b = [(x,y,z) for x in range(1,3) for y in range(3) for z in range(5)]
print(b)
print('-'*75)
c = [x for x in range(3,30) if x%2!=0]
print(c)
