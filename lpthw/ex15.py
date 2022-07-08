from sys import argv 

script, filename = argv #获取文件名 需要输入

txt = open(filename) # TXT变量 打开 读取文件 文件名为argv里如数的参数：那个.txt的文件名，open 用于打开文件的内置函数，使用OPEN的时候记得需要先关闭文件，如果是打开状态无法调用打开

print(f"Here's your file {filename}:") 
print(txt.read())

print("Type the filename again:")
file_again = input(">>")

txt_again = open(file_again)

print(txt_again.read())

print(txt_again.close())
