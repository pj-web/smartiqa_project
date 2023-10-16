class Cat:
    age: int = 2
    breed: str = 'Bengal'


print(getattr(Cat, 'breed'), getattr(Cat, 'age'))


tom = Cat()

setattr(tom, 'age', 1)

print(tom.__dict__, tom.age)


class Car:
    speed: float = 90.0
    color: str = 'red'


print(Car.speed, Car.color)

del Car.speed

print(Car.__dict__)