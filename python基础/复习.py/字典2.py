info = {
    "stull01":"alen zhang",
    "stull02":"si li",
    "stull03":"san zhang",
      }
#查
print(info)
print(info["stull01"])
print(info.get("stull04"))      
print("stull03" in info)

#改
info["stull02"] = "李四"
print(info)

#增
info["stull04"] = "小王"
print(info)

#删
del info["stull04"]     
info.pop("stull03")     
test1 = info.popitem()          
print(info)
print(test1)
