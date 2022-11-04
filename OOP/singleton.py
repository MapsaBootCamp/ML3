class Singleton(type):
    __instance = {}

    def __call__(self, *args, **kwds):
        if self not in Singleton.__instance:
            Singleton.__instance[self] = super().__call__(*args, **kwds)
        print(Singleton.__instance)
        return Singleton.__instance[self]


class B(metaclass=Singleton):
    pass


class A(metaclass=Singleton):
    # __instance = None

    def __init__(self, name) -> None:
        self.name = name

    # @classmethod
    # def __new__(cls, *args, **kwargs):
    #     if not cls.__instance:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance


a1 = A("a1")
a2 = A("a1")


b1 = B()
b2 = B()


print(a1 is a2)

print(a1 is b1)

print(b1 is b2)
