from sys import argv #将从SYS中取出argv功能
# read the WYSS section for how to run this
script, first, second, third = argv  #argv 中有3个参数第一个是库名 

print(">>>> argv=",repr(argv))# 打印 argv 读取 argv repr()函数就是将对象转化为供解释器读取的形式

age = input("How old are you?")
height = input("How tall are you ?")
weight = input("How much do you weight?")

print(f"So,you're{age} old, {height} tall and {weight} heavy.")

print("The script is called:",script) #打印这个4个参数 第一个为脚本名
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)


