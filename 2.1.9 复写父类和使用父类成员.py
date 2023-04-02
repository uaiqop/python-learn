"""
重新定义父类的属性和方法
"""

class year_2021:
    hello = "hello,2021"
    def say_hello(self):
        print(self.hello)
        print("你好，2021")

class year_2022(year_2021):
    hello = "hello,2022"
    def say_hello(self):

        print(self.hello)
        print("你好，2022")
        # 调用父类原本的成员
        print(f"父类：{year_2021.hello}")


year = year_2022()
year.say_hello()

