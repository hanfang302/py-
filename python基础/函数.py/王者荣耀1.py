wzry = "王者荣耀管理系统"
print(wzry.center(35))
print("*"*45)
print("功能1:%s\n功能2:%s\n"%("注册,登录"))
print("*"*45)
account_list = [{"name":"zhangsan","passwd":"123456"}]
def login(account="zhangsan",passwd="123456"):
    print("登录")
    for dic in account_list:
        if account == dic["name"]:
            if dic ["passwd"] == passwd:
                print("登录成功")
            else:
                print("密码错误")
        else:
            print("帐号输入错误")
def register(zhanghao="lisi",mima="456789"):
    print("注册")
    for dic in account_list:
        if dic["name"] == zhanghao:
            print("帐号已经被注册")
        else:
            xinxi = {}
            xinxi["name"]=zhanghao
            xinxi["passwd"]=mima
            account_list.append(xinxi):
            print("帐号注册成功")
            break
print("*"*45)
account = input("请输入帐号")
passwd = input("请输入密码")
login(account,passwd)
print("*"*45)

