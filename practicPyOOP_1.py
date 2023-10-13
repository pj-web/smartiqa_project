class PersianCat:
    breed = 'persian'  # attribute of this class
    age = 12.0


class SiberianCat:
    breed = 'siberian'
    age = 0.5


class BengalCat:
    breed = 'bengal'
    age = 2.0


tom = PersianCat()
garfield = SiberianCat()
maxim = BengalCat()

# print(type(tom), type(garfield), type(maxim), sep='\n')
print(isinstance(tom, BengalCat))



# class Hamster:
#     color = "white"
#
#
# tom = Hamster()
# print(id(tom))

# class MyClass:
#   x = 5
#   y = 7
#
#
# p1 = MyClass()
# print(p1)
