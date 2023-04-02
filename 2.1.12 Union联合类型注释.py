"""
在容器里面出现多种类型，不方便注释时，可以使用联合类型注释
"""
from typing import Union

my_list: list[Union[str, int]] = [1, "hello", 4, 6, 20, "world"]
my_dict: dict[Union[str, int]] = {"name": "Aaron", "age": 17}


def hello(say: Union[str, int]) -> Union[str, int]:
    pass
