# Welcome to Esu Struct!


[![Build Status](https://travis-ci.org/torokmark/esu.svg?branch=master)](https://travis-ci.org/torokmark/esu)
[![Documentation Status](https://readthedocs.org/projects/esu/badge/?version=latest)](https://esu.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/esu.svg?color=blue)](https://pypi.org/project/esu/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/esu.svg)](https://github.com/torokmark/esu)
[![PyPI - License](https://img.shields.io/github/license/torokmark/esu)](https://github.com/torokmark/esu/blob/master/LICENSE.md)


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

