# 定义一个整数型变量
int1 = 5
# 将整数型转换为字符串
int_str = str(int1)
# 验证
print(type(int_str), int_str)

# 定义一个浮点型变量
float1 = 3.14
# 转换为字符串
float_str = str(float1)
# 验证
print(type(float_str), float_str)

# 转换为整数型
str_int = float("11.23")
# 验证
print(type(str_int), str_int)

# 整数转换为浮点数
int_float = float(114)
print(type(int_float), int_float)

# 浮点数转换为整数,小数会被去掉
float_int = int(114.5)
print(type(float_int), float_int)

