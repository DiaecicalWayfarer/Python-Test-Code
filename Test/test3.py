# 列表打印
names=["小李","小张","小王"]
greeting1="你好，"
greeting2="，能不能共进晚餐！"
print(names[1]+"，无法赴约")
names[1]="小丁"
print("找到了一张更大餐桌")
names.insert(0,"小韩")
names.insert(2,"小明")
names.append("小徐")
print(greeting1+names[0]+greeting2)
print(greeting1+names[1]+greeting2)
print(greeting1+names[2]+greeting2)
print(greeting1+names[3]+greeting2)
print(greeting1+names[4]+greeting2)
print(greeting1+names[5]+greeting2)
print("只能邀请两位嘉宾！")
print("非常抱歉，"+names.pop()+",无法邀请你共进晚餐")
print("非常抱歉，"+names.pop()+",无法邀请你共进晚餐")
print("非常抱歉，"+names.pop()+",无法邀请你共进晚餐")
print("非常抱歉，"+names.pop()+",无法邀请你共进晚餐")
print(greeting1+names[0]+"你依旧在邀请之列")
print(greeting1+names[1]+"你依旧在邀请之列")

del names[0]
del names[1]
print(names)

# 列表排序
places=["北京","天津","上海","广东","深圳"]
print("原始列表：")
print(places)
print("临时修改列表：")
print(sorted(places))
print("再次打印列表：")
print(places)
print("反顺序列表：")
places.reverse()
print(places)
print("恢复原始列表：")
places.reverse()
print(places)
print("列表排序：")
places.sort()
print(places)
print("列表反排序：")
places.sort(reverse=True)
print(places)
