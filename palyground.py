# Unlimited Positional Arguments
def add(*args):  # args is a tuple
    total = 0
    for n in args:
        total += n
    return total


print(add(1,2,3,4,5,6,7,8,9,10))


# Unlimited keyword Arguments
def calculate(n, **kwargs):  # kwargs is a dictionary
    print(kwargs)
    print(kwargs["add"])
    for (key, value) in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(7, add=3, multiply=5))


class Car:
    def __init__(self, **kwargs):  # kwargs is a dictionary
        # self.make = kwargs["make"]  # Use for REQUIRED arguments
        # self.model = kwargs["model"]  # Will cause KeyError if argument not given

        self.make = kwargs.get("make")  # get() returns None if the argument is not given
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats", 4)  # Default value to return if argument not given


my_car = Car(make="Nissan", color="red")
print(my_car.seats)
