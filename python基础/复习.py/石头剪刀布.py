player = int(input('请出拳 石头(1),剪刀(2),布(3):'))
computer = 2
if ((player == 1 and computer == 2) or
     (player == 2 and computer == 3) or
     (player == 3 and computer == 1)):
    print('电脑输了')
elif player == computer:
    print('心有灵犀，再来一局')
else:
    print('不行，我要和你决战到底')
