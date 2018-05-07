"""
名片管理系统
1.添加一个新的名片
2.删除一个名片
3.修改一个名片
4.查询一个名片
5.显示所有名片
6.退出系统
"""
# 有一个容器来存储名片 用list用来存储数据
card_infors = []
while True:
    # 获取用户输入用户的内容
    num = int(input('请输入操作序号'))
    # 根据用户输入的序号，进行相应的操作
    if num==1: # 添加内容
        new_name = input('请输入新的名字:')
        new_wechat = input('请输入微信:')
        new_qq = input('请输入qq帐号:')
        new_addr = input('请输入地址:')
        new_tel = input('请输入电话:')

        # 定义一个新的字典 用来存储新的名片
        # 方法一
        #new_infor = {}
        #new_infor['name'] = new_name
        #new_infor['wechat'] = new_wechat
        #new_infor['qq'] = new_qq
        #new_infor['addr'] = new_addr
        #new_infor['tel'] = new_tel
        # 方法二
        new_infor= {'name':new_name,'wechat':new_wechat,'qq':new_qq,'addr':new_addr,'tel':new_tel}
         # 把字典添加到列表里面
        card_infors.append(new_infor)
        # 添加成功
        #print('添加成功，现在的全部数据是%s'%card_infors)
        for name in card_infors:
            print('*'*20)
            for k,v in name.items():
                print('%s:%s'%(k,v)) 
    elif num == 2: # 删除一个名片
        name = input('请输入要删除的名片')
        for dic in card_infors:
            if 
                print('该用户已被删除')
    elif num == 3: # 修改一个名片
        pass
    elif num == 4: # 查迅一个名片
        temp = input('请输入您要查询的名片')
        for dic in dic_infors:
            if temp in dic.values():
                 print('该用户存在')
            else:
                print('该用户不存在')
    elif num == 5: # 显示所有名片
        for dic in card_infors:
            print('*'*20)
            for k,v in dic.items():
                print('%s:%s'%(k,v))
    else:
        break
        print('退出循环')
