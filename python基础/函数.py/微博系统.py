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

# 定义两个函数（用户和密码）
def register(name='张三',passwd='123456'):
    #注册               
    for dic in account_list:
        if account == dic['name']
            print('帐号已被注册，请从新注册')
        else:
            #创建一个字典，用来存储注册的帐号和密码
            new_user = []
            #把用户注册的帐号存入字典当中
            new_user['account']=name
            #把用户注册输入的密码存入字典当中
            new_user['passwd']=passwd
            #把创建的字典加入到列表当中
            account_list.append(new_user)
            print('帐号创建成功')    
            break
            print('*'*45)
#系统默认一个帐号
account_list = [{'name':'张三','passwd':'123456'}]
#定义两个函数（用户和密码）
def login(account='张三','passwd'='123456'):
     #登录
    for dic in account_list:
        if account == dic['name']:




def addUser():
    #添加用户
    pass






def changeUser():
     #修改用户
    pass





def deleteUser():
     #删除用户
    pass




def queryUser():
     #查询用户
    pass





def exit():
    #退出账号
    pass
