types_of_people = 10 #将typeS_of_people赋值为10
x = f"There are {types_of_people} types of people." #将X赋值为XX引用上面的变量types_of_people

binary = "binary"#将左侧赋值为右侧
do_not = "don't" #将左侧赋值为右侧
y = f"Those who know {binary} and those who {do_not}." #将Y赋值为XX引用上面的两个变量
print(">>>> after assign y",y)

print(x) #打印X
print(y) #打印y

print(f"I said:{x}") #打印字符串 这里用的f-string
print(f"I also said:'{y}'") #打印字符串 这里用的f-string

hilarious = "False" #将左侧赋值为右侧
joke_evaluation = "Isn't that joke so funny?! {}" #将左侧赋值为右侧

print(joke_evaluation.format(hilarious)) #打印 并引用format()的格式化方法

w = "This is the left side of..."  #将左侧赋值为右侧
e = "a string with a right side."  #将左侧赋值为右侧

print(w + e) #将打印W+e