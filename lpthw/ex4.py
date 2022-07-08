# 变量和命名
cars = 100 #cars等于 100，是将100取名为cars
space_in_a_car = 4.0 # 将4.0 取名为space_in_a_car
drivers = 30 # 将30取名为drivers
passengers = 90 # 将90取名为passengers
cars_not_driven = cars - drivers # 将公式 cars-drivers 取名为 cars not driver 这里_下划线代表了空格，因为python无法用空格取名
cars_driven = drivers #将drivers 取名为cars_driver
carpool_capacity = cars_driven * space_in_a_car #将cars_driven *space_in_a_car的结果 命名为左侧的名字，结果为浮点数，因为space_in_a_car为浮点数
average_passengers_per_car = passengers / cars_driven #passengers / cars_driven 的结果命名为左侧的名字，浮点数，因为除法结果在python中为浮点数


print("There are", cars, "cars available")
print("There are only",drivers,"drivers arailable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")