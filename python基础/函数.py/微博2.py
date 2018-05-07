'''
微博
1.功能提示
2.开始业务逻辑
  1.注册/登录
  2.添加用户
  3.修改用户
  4.删除用户
  5.查询用户
  6.退出帐号
'''
mb = '微博系统功能提示'
print(mb.center(35))
print('*'*45)
print('功能1:%s\n功能2:%s\n'%('注册','登录'))
print('*'*45)
  
# 用一个列表来存储用户的帐号和密码
  
account_list = []

#定义两个函数（用户和密码）
def login(account='张三',passwd='123456'):
    #登录
    print('登录')
    account = input('请输入帐号')
    passwd = int(input('请输入密码'))
    for dic in account_list:
        if account == dic['account']:
            #说明帐号正确，接下来进行密码判断
            if dic['passwd'] == passwd:
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('帐号输入错误，请重新输入')
            print('*'*45)
# 定义个函数（用户和密码）
def register(zhanghao='张三',mima='123456'):
      #注册
    print('注册')               
    for dic in account_list:
        if dic['account']== zhanghao:
            print('帐号已被注册，请从新注册')
        else:
            #创建一个字典，用来存储注册的帐号和密码
            new_user = {}
            #把用户注册的帐号存入字典当中
            new_user['account']=zhanghao
            #把用户注册输入的密码存入字典当中
            new_user['passwd']=mima
            #把创建的字典加入到列表当中
            account_list.append(new_user)
            print('帐号创建成功')
            print('*'*45)
   
    #添加用户  
def addUser():
    print('添加帐号')
    name = input('请输入用户名')
    passwd = input('请输入密码')
    #把新用户的的帐号相关信息封装起来
    #用户帐号信息进行封装变量名
    message = {'用户名':name,'密码':passwd}
    #把封装的变量（字典）移动到刚开始创建的列表当中
    account_list.append(message)
    print('*'*45)
    print('现有帐号%s'%account_list)
    print('*'*45)
def changeUser():
    #修改用户
    print('需要修改的内容')
    account = input('请输入要修改的帐号用户名')
    count = 0
    for dic in account_list:
        if dic['姓名']==name:
            account_list[count]['用户名'] = input('请输入姓名')
            account_list[count]['密码'] = input('请输入密码')
        else:
            count += 1
            print('*'*45)
def deleteUser():
    #删除用户
    print('删除')
    account = input('请输入要删除的帐号用户名')
    #相当于计数器
    count = 0
    for dic in account_list:
        if dic['用户名'] == name:
            del account_list[count]
        else:
            count += 1
    print('此时还有%s'%account_list)
    print('*'*45)
def queryUser():
    print('查询')
    #查询用户
    for dic in account_list:
        print('用户名%s\t密码%s\t'%(dic['用户名'],dic['密码']))
        print('*'*45)
def exit():
    #退出账号
    print('退出')


#调用函数
login()
register()
addUser()
changeUser()
deleteUser()
queryUser()
exit()

