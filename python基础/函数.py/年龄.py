age = int(input("请输入年龄"))
if age <2:
    print("婴儿")
elif age>=2 and age<4:
    print("学步")
elif age>=4 and age<13:
    print("儿童，可以参加六一儿童节")
elif age>=13 and age<20:
    print("青少年")
elif age>=20 and age<65:
    print("成年人")
else:
    print("不是地球人")
