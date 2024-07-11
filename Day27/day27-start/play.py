# def add(*nums):
#     sum = 0
#     for i in nums:
#         sum += i
#     return sum
#
# print(add(6,3,8))


# def calculator(n, **kwargs):
#     # print(kwargs)
#     # for key,value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["mul"]
#     n -= kwargs["sub"]
#     print(n)
#
# calculator(5, add=2, sub=1, mul=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
