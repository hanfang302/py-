# 输入信息:
def message(name,gender,age,number):
    f = open('name.txt','w+')
    f.write(name)
    f.close()
    f2 = open('gender.txt','w+')
    f.write(gender)
    f.close()
    f3 = open('age.txt','w+')
    f.write(age)
    f.close()
    f4 = open('number.txt','w+')
    f.write(number)
    f.close()

# 输出信息:
def out_message(name,gender,age,number):
    f = open('name.txt','r')
    f2 = open('gender.txt','r')
    f3 = open('age.txt','r')
    f4 = open('number.txt','r')
    f.close()
    f2.close()
    f3.close()
    f4.close()
