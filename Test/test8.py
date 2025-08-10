#  喜欢的图书

# def favoritr_book(title):
#     """喜欢的图书"""
#     print(f"我喜欢的图书是{title}")
# favoritr_book("三体")

#  城市

# def describe_city(city,country="China"):
#     """描述城市"""
#     print(f"{city} is  in {country}")
# describe_city("BeiJing")
# describe_city("ShangHai","China")
# describe_city("Washington","USA")

# 姓名  

# def get_formatted(first_name,last_name):
#     """返回规范格式的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\n请输入姓名：")
#     print("请输入q退出")
#     f_name=input("请输入名：")
#     if f_name=="q":
#         break
#     l_name=input("请输入性：")
#     if l_name=="q":
#         break
#     formatted_name=get_formatted(f_name,l_name)
#     print(formatted_name)

# 消息

def show_messages(messages):
    """显示消息"""
    for message in messages:
        print(message)
def send_messages(messages,sent_messages=None):

    """发送消息"""
    if sent_messages is None:
        sent_messages = []
    for message in messages:
        sent_messages.append(message)
    for sent_message in sent_messages:
        print(f"发送消息：{sent_message}")

messages = ["hello","world","python"]
show_messages(messages)
send_messages(messages,sent_messages=None)





