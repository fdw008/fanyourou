name = 'Wei Da.Fan'
age = 36 # not a lie
height = round(90 * 2.54) #  将英寸转化成厘米，所以乘以2.54 将结果四舍五入
weight = round(180 * 0.453) #  将磅转化成千克 ,所以乘以0.453 将结果四舍五入
eyes = 'Black'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")# 在打印的文字中引用变量，需要用到格式化，即f"X{引用的变量名}"
print(f"He's {height} centimeter tall.")
print(f"He's {weight} kilogram heavy.")
print("Actually that's not too heavy.")
print(f"He' got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height +weight
print(f"If I add {age}, {height} , and {weight} I get {total}.")