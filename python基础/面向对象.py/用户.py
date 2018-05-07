class User:
    def __init__(self,):
        self.first_name = '张'
        self.last_name = '三'

    def describe_user(self):
        print(self.first_name,self.last_name)
    
    def greet_user(self): 
        print('你好，我叫张三')


UX = User()
UX.describe_user()
UX.greet_user()
