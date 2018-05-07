def number(a):
    print('修改前的:',a)
    a+=1
    print('修改后的:',a)
    #return a
a = 3
print('函数内部操作后的a:',number(a))
print('函数外部的变量a:',a)

