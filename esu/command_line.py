from esu import Struct, OpenStruct

def main():
    Dog = Struct(
            'Dog', 
            'name', 'age', 
            methods={
                'say': lambda self: print("Hello {}".format(self.__dict__['name']))
            })

    d = Dog()
    d.name = 'rex'
    d.age = 54
    d.say()
    print(d.members())
    
    d2 = Dog()
    d2.name = 'Wolfie'
    d2.age = 22 
    print('Age: {}'.format(d2.age))
    d2.say()

    d3 = Dog()
    d3.name = 'Wolfie'
    d3.age = 22
    d3.say()
    print('d2 == d3', d2 == d3)

    h = {}
    h[d] = 1
    h[d2] = 2
    h[d3] = 3
    print(len(h))

    o = OpenStruct()
    o.dog_name = 'Rex'
    print(o.dog_name)
    print(o)

    b = OpenStruct({'age':12})
    print(b.age)


if __name__ == "__main__":
    main()
