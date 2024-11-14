from cat import Cat
from dog import Dog

my_cat = Cat("Rominet",age=79)

cat2 = Cat(age=45)
cat2.name = 'bertolt'
cat2.legs-=1
print(cat2.name, cat2.legs,cat2.get_age())
print(my_cat.get_age())

my_dog = Dog(name='Chien')
my_dog.speak()
my_dog.eat()
my_cat.eat()

