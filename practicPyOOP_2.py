class Person:
    age = 16
    name = 'Max'


# print(Person.name)
# print(getattr(Person, 'x', 'Impossible'))

setattr(Person, 'name', 10)
print(Person.name)

print(Person.__dict__)

setattr(Person, 'color', 'carroty')
