# class Person:
#     age = 18
#     height = 175
#
#
# Person_1 = Person()
#
# print(Person.__dict__)
# print(Person_1.__dict__)


class Person:
    age: int = 20
    height: int = 170


Person_1 = Person()
Person_2 = Person()

Person_1.height = 160
Person_2.hair_color = 'black'

print(Person_1.__dict__)
print(Person_2.__dict__)
print(Person)
