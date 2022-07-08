from sys import argv #将从SYS中取出argv功能

script, user_name = argv   #argv 中有2个参数第一个是库名 
promp = '>'            #赋值 变量

print(f"Hi {user_name},I'm the {script} script.") #打印 绝对值引用f“{}”
print("I'd like to ask you a few questions.")  #打印
print(f"Do you like me {user_name}?") #打印 绝对值引用f“{}”
likes = input(promp)                  #likes赋值 输入交互内容 在>后

print(f"Where do you live {user_name}?")  #打印 绝对值引用f“{}”
lives = input(promp)               #lives 输入交互内容 在>后

print("What kind of computer do you  have?")
computer = input(promp)

print(f"""
Alright, so you said {likes} about liking me.
you live in {lives}.Not sure where that is.
And you have a {computer} computer. Nice.
""")
