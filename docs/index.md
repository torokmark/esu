# Welcome to Esu Struct!

Enjoy the flexibility of structs with *esu*!

You can create types on the fly with previously declared fields and methods by using *esu struct*.  
The created type additionally contains methods for equation, hashing and string representation.

### Install

```sh
pip install esu
```

### Usage

```py
from esu import Struct

Dog = Struct('Doggy', 
             'name', 'age', 
             methods={
                 'say': lambda self: print("Hello {}".format(self.__dict__['name']))
            })

d = Dog()
d.name = 'Rex'
d.age = 5
d.say() # => Hello Rex
```

### Documentation

For further information, read the documentation that can be found: [https://esu.readthedocs.io](https://esu.readthedocs.io)

### Contribution

1. Fork it!
2. Make your changes!
3. Send a PR!

