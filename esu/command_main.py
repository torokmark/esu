from esu import Struct

Dog = Struct('Doggy', 
             'surname', 'age', 
             methods={
                 'say': lambda self: print("Hello {}".format(self.__dict__['surname']))
            })

d = Dog()

d.surname = 'rex'
d.age = 54

print(Dog.__name__, d.surname)
d.say()

d2 = Dog()
d2.surname = 'Wolfie'
d2.age = 22 
print('Age: {}'.format(d2.age))
d2.say()

d3 = Dog()
d3.surname = 'Wolfie'
d3.age = 22
d3.say()
print('=======', d3 == d2)
print(d3)

h = {}
h[d] = 1
h[d2] = 2
h[d3] = 3
print(h)
