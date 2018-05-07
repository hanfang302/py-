class Person(object):
    def __init__(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def _work(self):
        print('工作')

    def __awauy(self):
        print('away')

class Student(Person):
    def constrcution(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)
 
    @staticmethod
    def testbug():
        _Bug

    @staticmethod
    def _Bug(object):
        def showbug():
            print('showbug')


s1 = Student('李四',18,'football')
s1.showperson()
print('--------')
# 无法访问__taste 报错
s1.constrcution('王五'，20,'basketball')
s1.showperson()
s1.showstudent()
print('-'*45)
s1.showstudent()
print('-'45)
s1.restbug()

