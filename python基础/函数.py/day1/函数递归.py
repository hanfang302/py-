def one(num)
    if num >= 1:
        result = num * one(num-1)
    else:
        result = 1
    return restlt
ret = one(3)
print(ret)



 
