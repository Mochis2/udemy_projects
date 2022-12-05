def add(*args): # -----------positional arguments
    return sum(args)
    






print(add(3, 3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,32,23,4,4,4))



def add1(*args):
    print(args)



add1(2,34,25,2,5,2,5235,3)


def calculate(n, **kwargs): # ---------------------keyword arguments
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("colour")
        self.seats = kw.get("seats")



my_car = Car(make="Nissan", colour="brown")
print(my_car.model)
print(my_car.make)
print(my_car.color)