"""
在新的类中继承一个类中的所有内容
"""

class year_2021:
    year = 2021
    def say_hello(self):
        print(f"hello,{self.year}")


# 继承上面的year_2021
class year_2022(year_2021):
    hello = "hello,2022"
    def say_hello_2022(self):
        print(self.hello)

year = year_2022()
year.say_hello()
year.say_hello_2022()
# 支持继承多个类，用逗号分隔
# 如果多继承下父类成员名相同，则靠左的类优先
