<h1 id="esu.struct.Struct">Struct</h1>

```py
Struct(self, cls, *fields, methods={})
```

## Cls

Name of the created type.

## Fields

List of fields that would be available on the instance.

```py
Dog = Struct('Dog', 'name', 'age')
dog = Dog()
dog.name = 'caesar'
dog.age = 6
```

## Methods

Methods that are bound to the type. That is passed as dictionary, where *key* is
the name of the method, and *value* is a lambda expression which is executed
when method is called.

```py
Dog = Struct('Dog', 
             'name', 'age', 
             methods={
                 'say': lambda self: print("Hello {}".format(self.__dict__['name']))
            })

dog = Dog()
dog.name = 'Rex'
dog.say() # => Hello Rex
```

## ==

Two instance of created type are equivalent if both fields are equivalent.

If `__eq__` is passed via `methods`, it overwrites the default one.

## hash

Hash of an instance is based on the its fields and values.

If `__hash__` is passed via `methods`, it overwrites the default one.

## str

String representation of an instance is based on the its fields and values.

If `__str__` is passed via `methods`, it overwrites the default one.









