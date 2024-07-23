from abc import ABC
from typing import Any


class Singleton(ABC):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    # just a different way of doing it
    @classmethod
    def get_instance(cls):
        return cls._instance

    @property
    def id(self):
        return id(self)


class MyClass(Singleton):
    pass


if __name__ == '__main__':
    obj_1 = MyClass()
    obj_2 = MyClass()
    obj_3 = MyClass.get_instance()

    print(obj_1, obj_2, obj_3, obj_1.id == obj_2.id == obj_3.id)
