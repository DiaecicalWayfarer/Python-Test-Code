#  餐馆

# class Restaurant:
#     """餐馆"""
#     def __init__(self,resturant_name,cuisine_type):
#         """初始化餐馆"""
#         self.resturant_name = resturant_name
#         self.cuisine_type = cuisine_type
#     def describe_resturant(self):
#         """描述餐厅"""
#         print(f"餐厅名称：{self.resturant_name}")
#         print(f"餐厅类型：{self.cuisine_type}")
#     def open_resturant(self):
#          """打开餐厅"""
#          print(f"{self.resturant_name}正在营业，欢迎来到{self.cuisine_type}餐厅")    
# restaurant = Restaurant("张三餐厅","中国")
# restaurant.describe_resturant()
# restaurant.open_resturant()

#  就餐人数

# class Restaurant:
#     """餐馆"""
#     def __init__(self,resturant_name,cuisine_type):
#         """初始化餐馆"""
#         self.resturant_name = resturant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#     def set_number_served(self,number_served):
#         """设置就餐人数"""
#         self.number_served=number_served
#     def increment_number_served(self,number_served):
#         """增加就餐人数"""
#         self.number_served+=number_served
# taotaoju=Restaurant("陶陶居","中国")
# print(taotaoju.resturant_name)
# print(taotaoju.cuisine_type)
# print(taotaoju.number_served)
# taotaoju.set_number_served(100)
# taotaoju.increment_number_served(20)
# print(taotaoju.number_served)

# 冰淇淋小店

# class Restaurant:
#     """餐馆"""
#     def __init__(self,resaturant_name,cuisine_type):
#         """初始化餐馆"""
#         self.resturant_name = resaturant_name
#         self.cuisine_type = cuisine_type
#     def describe_resturant(self):
#         """描述餐厅"""
#         print(f"餐厅名称：{self.resturant_name}")
#         print(f"餐厅类型：{self.cuisine_type}")
#     def open_resturant(self):
#          """打开餐厅"""
#          print(f"{self.resturant_name}正在营业，欢迎来到{self.cuisine_type}餐厅")
# class IceCreamStand(Restaurant):
#     """冰淇淋 Stand"""
#     def __init__(self,resturant_name,cuisine_type):
#         """初始化冰淇淋 Stand"""
#         super().__init__(resturant_name,cuisine_type)
#         self.flavors = ["vanilla","chocolate","strawberry"]
#     def show_flavors(self):
#         """显示冰淇淋口味"""
#         print("我们的冰淇淋口味有：")
#         for flavor in self.flavors:
#             print(flavor)
# so_icecream = IceCreamStand("张三冰淇淋","中国")
# so_icecream.show_flavors()
 
 
