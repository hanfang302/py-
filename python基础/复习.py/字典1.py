dict1 = {  
    'key':'value',  
    'key1':'value1'  
}  
a = [('key1','value1'),('key2','value2')]  
dict1 = dict(a)  
dict1 = {}.fromkeys(['key1','key2'],'default_value') #从键值创建dict  
dict1 = dict(key1='value1',key2='value2')  
  
#增加  
dict1['key3']='value3' #字典可以自动添加  
dict1.setdefault('key5','N/A') #如果不存在，就设置默认值  
  
#删除  
del dict1['key3']  
print dict1.pop('key2')  #popitem随机删除 和列表的pop一样  
#dict1.clear()  #深删除,即使有拷贝 也会被删除  
  
#修改  
if 'key1' in dict1:  
    dict1['key1']='new_value_1'  
#查找  
if 'key1' in dict1:  
    print dict1['key1']  
if dict1.has_key('key1'):  
    print dict1['key1']  
print dict1.get('key3','not exists') #宽松访问  
print dict1.keys(),dict1.values()  
  
#拼接  
dict2 = dict(key4 = 'value4') #从字典更新另一个字典  
dict1.update(dict2)  


