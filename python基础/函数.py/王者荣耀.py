'''
王者荣耀
1.功能提示，提示这个系统有哪些功能
2.开始业务逻辑
3.退出
'''
wzry_gnts = '王者荣耀系统功能提示'
print(wzry_gnts.center(30))
print('*'*45)
print('功能1:%s\n能2:%s\n'%('注册','登录'))
print('*'*45)

# 用一个列表来存储用户的帐号和密码
# 系统默认一个帐号信息
account_list = [{'name':'libai','passwd':'123456'}]
# 定义两个函数（用户和密码）
def login(account='libai',passwd='123456'):
      for dic in account_list:
        if account == dic['name']:
        # 说明用户输入的帐号和系统默认的帐号一样，帐号已经正确，接下来判断密码是否正确
            if passwd == dic['passwd']:
            # 同等用户输入的密码和系统默认的密码一样，那么登录成功
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('帐号输入错误')

def register(zhanghao='张三',mima='1234567'):
    # 注册
    for dic in account_list:
        if account == dic['name']:
            print('帐号已被注册，请重新注册')
        else:
            # 创建一个字典，来存储重新注册测的帐号密码信息
            tempDic = {}
            # 把用户输入输入的信息存储到临时创建的字典当中
            tempDic['account']=zhanghao
                    # 帐号      
            tempDic['passwd']=mima
                    # 密码           
            # 把新创建的字典加入到列表当中
            account_list.append(tempDic)
            print('帐号创建成功')
            break

