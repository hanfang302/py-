print('欢迎来到召唤师峡谷！')
msg = '欢迎来到召唤师峡谷！'
print(msg)
name = 'wangzherongyao'
print(name.title()) # 首字母大写
print(name.upper()) # 全部大写
print(name.lower()) # 全部小写
print('-'*45)
first_name = '郑'
last_name = '州'
full_name = first_name+''+last_name
print(full_name)
print('尊敬的召唤师:'+full_name+', 欢迎来到召唤师峡谷！' )
print('-'*45)
print('欢迎来到召唤师峡谷！')
print('\t欢迎来到召唤师峡谷！') # 向后缩进一个单位
print('\n欢迎来到召唤师峡谷！') # 换行输出
print('-'*45)
msg = '努力有用的话，还要天才干什么？'
print(msg)
msg= msg.strip() # 移除了变量msg两端的空格
num = 2
msg=('尊敬的召唤师，您在这句对战中的综合评分位于第'+str(num)+'位！')
print(msg)
heroes = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
print(heroes)
print(heroes[0])
print(heroes[1])
print(heroes)
heroes[0]='狄仁杰'
print(heroes)
print('-'*45)
heroe = ['安琪拉','李白','杨戬','貂蝉']
print(heroe)
heroe.append('兰陵王')
print(heroe)
print('-'*45)
heroe = ['安琪拉','李白','杨戬','貂蝉']
heroe.insert(0,'兰陵王')
print(heroe)
print('-'*45)
heroe = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
print(heroe)
del heroe[0]
print(heroe)
print('-'*45)
heroe = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
print(heroe)
tail = heroe.pop()
print(heroe)
print(tail)
print('-'*45)
heroe = ['安琪拉','李白','杨戬','后羿','貂蝉']
print(heroe)
heroe.remove('后羿')
print(heroe)
print('-'*45)
heroe = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
heroe.sort()
print(heroe)
heroe = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
heroe.sort(reverse=True)
print(heroe)
heroe = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
print(heroe)
print(sorted(heroe))
print(heroe)
heroe = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
print(heroe)
heroe.reverse()
print(heroe)
heroe = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
len(heroe)
print('-'*45)
heroe = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
for a in heroe:
    print('您的队伍中由此英雄:'+a)
heroe = ['安琪拉','李白','杨戬','貂蝉','孙悟空']
for a in heroe:
    print(a+'是一个十分优秀的英雄！'+'\n')
print('-'*45)
for a in range(1,5):
    print(a)
num = list(range(1,6))
print(num)
print('-'*45)
pingfangji = []
for shuzi in range(1,11):
    pingfang = shuzi**2
    pingfangji.append(pingfang)
print(pingfangji)

num = [shuzi**2 for shuzi in range(1,11)]
print(num)
