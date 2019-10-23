from esu import Struct

def test_field_struct_declared_field_is_none():
    Dog = Struct('Dog', 'age')
    dog = Dog()
    assert dog.age == None

def test_field_struct_declared_fields_and_set_values():
    Dog = Struct('Dog', 'name', 'age')
    dog = Dog()
    dog.name = 'rex'
    dog.age = 12
    assert dog.name == 'rex' and dog.age == 12

def test_eq_two_structs_are_equivalent():
    Dog = Struct('Dog', 'name', 'age')
    d1 = Dog()
    d1.name = 'rex'
    d1.age = 12
    d2 = Dog()
    d2.name = 'rex'
    d2.age = 12
    assert d1 == d2

def test_eq_two_structs_are_not_equivalent():
    Dog = Struct('Dog', 'name', 'age')
    d1 = Dog()
    d1.name = 'caesar'
    d1.age = 20
    d2 = Dog()
    d2.name = 'rex'
    d2.age = 12
    assert d1 != d2

def test_hash_two_structs_produce_different_keys():
    Dog = Struct('Dog', 'name', 'age')
    d1 = Dog()
    d1.name = 'rex'
    d1.age = 12
    d2 = Dog()
    d2.name = 'caesar'
    d2.age = 20
    hsh = {}
    hsh[d1] = 1
    hsh[d2] = 2
    assert len(hsh) == 2

def test_hash_two_structs_produce_the_same_key():
    Dog = Struct('Dog', 'name', 'age')
    d1 = Dog()
    d1.name = 'rex'
    d1.age = 12
    d2 = Dog()
    d2.name = 'rex'
    d2.age = 12
    hsh = {}
    hsh[d1] = 1
    hsh[d2] = 2
    assert len(hsh) == 1

def test_str_struct_str():
    Dog = Struct('Dog', 'name', 'age')
    dog = Dog()
    dog.name = 'rex'
    dog.age = 12
    assert '[name=rex, age=12]' == str(dog)

def test_method_struct_defined_method():
    Dog = Struct('Dog', 'name', 'age',
            methods={'say': lambda self: self.__dict__['name']}) 
    dog = Dog()
    dog.name = 'rex'
    dog.age = 12
    assert dog.say() == 'rex'

