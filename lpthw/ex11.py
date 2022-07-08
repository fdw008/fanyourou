print("How old are you?", end=' ') #end=''这个命令的意思是让下一行输出的内容不换行
age = int( input()) #输入函数 input 然后对input赋值 age 输入格式必须为整数int就是整数函数
print("How tall are you?", end='')
height = input() #输入函数 input 然后对input赋值 height
print("How much do you weigh?", end='')
weight = input() #输入函数 input 然后对input赋值 weight

print(f"so, you're {age} old, {height} tall and {weight} heavy,")#f"{}"绝对值，在文本中取赋值时使用，这里引用三个赋值age weigh heigh