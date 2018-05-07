# 注册的函数
def register(account,password):
    # 注册
    # 打开文件，以读的方式
    f = open('account.txt','r')
    # 读取内容
    acount_list = f.readlines()
    # 本地的帐号我已经取出，接下来我们需要判断本地的帐号是否存在，如果本地是一个空白的文件夹，什么都没有，那么就可以随便创建帐号，都不会重复。
    length = len(account_list)
    f.close()
    if length == 0:
        print('可以创建帐号')
        f = open('account.txt','w')
        f.write(account)
        f.close()
    else:
        names = []
        # 遍历 account_list 文件
  
