supper = ['小雪','小李','小刘']
print(supper[1] + ': 各位抱歉，因公事无法参加')
supper[1] = '王五'
print(supper)
print('各位，我找到一个更大的餐厅')
supper.insert(0,'小张')
supper.insert(2,'小红')
supper.append('小花')
print(supper)
print('很抱歉，各位。因为餐桌无法及时送到！只能邀请两位嘉宾。')
for num in range(0,4):
    number = 1
    number += 1
    n = supper.pop(number)
    print(n+ 'sorry')
print(supper)
print(supper[0]+ 'you can come party')
print(supper[1]+ 'you can come party')
del supper[0:]
print(supper)
#del supper[0]
#print(supper)
