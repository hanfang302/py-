#age = 22
#age_1 = 25
#if age >= 21 and age_1 >= 21:
    #print('正确')
#else:
    #print('年龄不够')

#age = 25
#age1 = 17
#if age >=20 or age1 >= 21:
    #print('通过')
#else:
    #print('未通过')

#toopings = ['andrew','caarolina','david']
#user = 'marie'
#if user not in toopings:
    #print(user.title() + ",you can post a response if you wish")


age = int(input('请输入，您的年龄'))
# 注释：年龄是数字类型一定要加int

if age >= 4 and age < 18:
    print('收费5美元')
elif age > 18 and age <= 65:
    print('收费10美元')
elif age > 65:
    print('打半折，收费5美元')
else:
    print('免费')
