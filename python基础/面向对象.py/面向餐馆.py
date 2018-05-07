class Restaurant:
    def __init__(self):
        self.restaurant_name = '张三餐厅'
        self.cuisine_type = '中餐厅'
        self.number_served =0

    def describe_restaurant(self):
        print(self.restaurant_name,self.cuisine_type)
    def open_restaurant(self):
        print('餐馆正在营业')
    def set_number_served(self,num):
        self.number_served = num       
        print(self.number_served)
    def increment_number_served(self,num): 
        self.number_served += num
        print('总人数为%d人'%self.number_served)
restaurant = Restaurant()
#print(restaurant.restaurant_name,restaurant.cuisine_type)
print('-'*50)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('-'*50)
restaurant1 = Restaurant()
restaurant1.describe_restaurant()
print('-'*50)
restaurant2 = Restaurant()
restaurant2.describe_restaurant()
print('-'*50)
restaurant3 = Restaurant()
restaurant3.number_served = 5
print(restaurant3.number_served)
print('-'*50)
restaurant3.number_served = 2
print(restaurant3.number_served)
print('-'*50)
restaurant3.set_number_served(6)
#restaurant3.increment_number_served(5)
restaurant3.increment_number_served(2)
