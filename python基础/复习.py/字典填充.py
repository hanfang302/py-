ponses = {}
# 设置一个标志，指出调查是否继续
active = True
while active:
    # 提示输入被调查的名字和回答
    name = input('\n请输入姓名？')
    ponse = input('Which mountain would you like to climb someday?')
    # 将回答存入字典当中
    ponses[name] = ponse
    # 是否还有要参与调查
    repat = input('Which mountain would you like to climb someday?(yes/no)')
    if repat == 'no':
        active = False

# 调查结果
print('\n-----Poll Results-----')
for name, ponse in ponses.items():
    print(name +' '+ 'would like to climb' + ponse + '.')
