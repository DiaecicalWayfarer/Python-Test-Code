# 餐馆定位
# people_num=input("请问有多少人？ ")
# people_num=int(people_num)
# if people_num>8:
#     print("没有空桌")
# else: print("有空桌")

# 10的整数倍

# num=input("请输入一个数：")
# num=int(num)
# if num % 10==0:
#     print("是10的整数")
# else:print("不是10的整数")

#  披萨配料

# user_input=input("请输入你想要的配料： ")
# while user_input!="quit":
#     print(f"好的，披萨里会为你添加{user_input}")
#     user_input=input("输入你想要的配料： ")

# 熟食店

sandwich_orders = ['金枪鱼三明治', '火腿奶酪三明治', '蔬菜全麦三明治']
finished_sandwiches = []
print("开始制作三明治...\n")
while sandwich_orders:
    current_order = sandwich_orders.pop(0)    
    print(f"正在制作: {current_order}")   
    finished_sandwiches.append(current_order)
    print(f"已完成: {current_order}\n")
print("\n所有三明治已完成:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
