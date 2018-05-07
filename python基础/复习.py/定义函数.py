def greet_user():
    print('hello')
greet_user()
print('-'*45)

# 传入形参及实参
def greet_user(username):
                # 形参
    print('hello!' + username.title() + '!')
# 调用（定义后的函数一定要进行调用，否则不会输出）
greet_user('jesse')
            # 实参
print('-'*45)

# 位置实参
def pet(animal_type, pet_name):
    print('\nI have a' + animal_type)
    print('My' + animal_type + "'s name is " + pet_name.title() + '.')
pet('hamster','harry')
print('-'*45)

# 调用多次函数
def pet(animal_type, pet_name):
    print('\nI have a' + animal_type + '.')
    print('My' + animal_type + "'s name is " + pet_name.title() + '.')
pet('hamster','harry')
pet('dog','willie')
print('-'*45)

# 关键字实参
def pet(animal_type, pet_name):
    print('\nI have a' + animal_type + '.')
    print('My' + animal_type + "'s name is " + pet_name.title() + '.')
pet(animal_type='hamster',pet_name='harry')
print('-'*45)

# 默认值
def pet(pet_name,animal_type='dog'):
    print('\nI have a' + animal_type + '.')
    print('My' + animal_type + "'s name is " + pet_name.title() + '.')
pet(pet_name='willie')
print('-'*45)

# 返回简单值
def name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = name('jimi','hendrix')
print(musician)
print('-'*45)

# 让实参变成可选的
def name(first_name,middle_name,last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = name('john','lee','hooker')
print(musician)
print('-'*45) 

def name(first_name,last_name,middle_name=''):
    if  middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = name('jimi', 'hendrix')
print(musician)
musician = name('john', 'hooker', 'lee')
print(musician)

# 返回字典
def person(first_name, last_name):
    person = {'first':first_name, 'last': last_name}
    return person
musician = person('jimi','hendrix')
print(musician)

