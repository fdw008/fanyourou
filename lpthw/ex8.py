formatter = "{} {} {} {}" #赋值格式化

print(formatter.format(1,2,3,4)) #打印格式化 1234,这里formatter已经赋值了“{}”所以，满足.format的格式要求 （格式要求为“{}”.format() ）
print(formatter.format("one", "two", "three", "four"))#打印格式化 1234
print(formatter.format(True,False,False,True))#打印格式化 真，假，真，假（这里因为true 和 false 是python里的关键字，所以无需用引号）
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))#这里的换行纯粹为了看这舒服，其实上如果不输入\n是不会换行的