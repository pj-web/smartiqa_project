# class Dog:
#     name = 'Sonia'
#     age = 6.3
#
#
# setattr(Dog, 'age', 5.5)
#
# print(Dog.age)
#
# print(Dog.__dict__)

# class Room:
#     width1 = 3000
#     width2 = 2500
#
#
# print(Room.width1 + Room.width2)


class House:
    pass


setattr(House, 'rooms', 4)

print(House.rooms)

House.bathrooms = 2

print(House.bathrooms)

print(House.__dict__)


class House:
    bedrooms = 3
    bathrooms = 2


print(House.bathrooms)

delattr(House, 'bathrooms')

print(getattr(House, 'bathrooms', 'There\'s no bathrooms'))

delattr(House, 'bedrooms')

print(House.__dict__)
