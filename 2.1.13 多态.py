"""
指的是多种状态，完成某种行为时，使用不同的对象会得到不同的状态
"""

class Year:
    def say(self):
        pass

class hello2021(Year):
    def say(self):
        print("hellp,2021")

class hello2022(Year):
    def say(self):
        print("hello,2022")

def hello(year: Year):
    year.say()

h2021 = hello2021()
h2022 = hello2022()

hello(h2022)
hello(h2021)

"""
以父类作定义声明
以子类作实际工作
"""

"""
父类的say方法是空实现，只是来确定有哪些方法，具体方法的实现，由子类自行决定
这种写法叫做抽象类
抽象类：含有抽象方法的类
抽象方法：方法体是空实现(pass)的方法
"""

"""
意义：
提出标准后，不同厂家各自实现标准的要求
"""