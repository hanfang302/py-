def xinxi(ziliao):
f = open('ziliao.txt','r')
ziliao_list = f.readlines()
lenght = len(ziliao_list)
f.close()
if ziliao_list == 0:
    print('可以添加学员文档')
    f = open('ziliao.txt','w')
    f.wrint(ziliao)
    f.close()
else:
