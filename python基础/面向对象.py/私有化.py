class Person(object):
    def __init__(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print('my _work')

    def __away(self):
        print('my __away')

class Student(Person):
    def construction(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def testbug():
        _Bug.shoebug()


class _Bug(object):
    @staticmethod
    def showbug():
        print('showbug')
    

a1 = Student('张三',20,'football')
a1.showperson()
print('*'*45)
