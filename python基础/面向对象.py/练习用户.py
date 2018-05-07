class User:
    def __init__(self):
        self.xing_name = '张'
        self.ming_name = '三'
        self.age = '20'
        self.address = '圣托里尼'
        self.login_attempts = 0

    def describle_user(self):
        print(self.xing_name,self.ming_name,self.age,self.address)

    def greet_user(self):
        print('CH欢迎你')
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts = 0

lisi = User()
lisi.xing_name = '李'
lisi.ming_name = '斯'
lisi.address = '瑞士'
lisi.describle_user()
lisi.greet_user()
print('-'*50)
ww = User()
ww.xing_name = '王'
ww.ming_name = '五'
ww.address = '荷兰'
ww.age = '25'
ww.describle_user()
ww.greet_user()

xm = User()
xm.increment_login_attempts()
xm.reset_login_attempts()
