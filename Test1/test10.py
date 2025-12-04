#   Python 学习笔记(读文件)

# from pathlib import Path
# path=Path("./learing_python.txt")
# content=path.read_text()
# print(content)
# lines=content.splitlines()
# for line in lines:
#     print(line)

# 访客薄(写文件)

# from pathlib import Path
# names=""
# user_input=input("请输入您的姓名(输入完成请按q停止程序):")
# while user_input!="q":
#     names+=user_input+"\n"
#     user_input=input("请输入您的姓名(输入完成请按q停止程序):")
# path=Path("./guest_book.txt")
# path.write_text(names)

# 加法运算（异常）

# user_input1=input("请输入第一个数字:")
# user_input2=input("请输入第二个数字:")
# try:
#     result=int(user_input1)+int(user_input2)
# except ValueError:
#     print("请输入合理的数字")
# else:
#     print(result)

# 用户字典（储存数据）

# from pathlib import Path
# import json
# path=Path("./username.json")
# if path.exists():
#     content=path.read_text()
#     user_dict=json.loads(content)
#     print(user_dict)
# else:
#     user_name=input("请输入您的用户名:")
#     age=int(input("请输入您的年龄:"))
#     sex=input("请输入您的性别:")
#     user_new_dict={
#         "username": user_name,
#         "age": age,
#         "sex": sex,
#         }
#     content=json.dumps(user_new_dict)
#     path.write_text(content)
#     for key,value in user_new_dict.items():
#         print(f"用户你好，您的{key}是{value}")




