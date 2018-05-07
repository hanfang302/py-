try:
    print('test1')
    open('123.txt','r')
    print('test2')
except IOError:
    pass

try:
    print(num)
except NameError:
    print('产生错误了')

print(1)
try:
    print(dd5)
except:
    print('出错了')
print(6)
print(4)
