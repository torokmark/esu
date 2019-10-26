<h1 id="esu.open_struct.OpenStruct">OpenStruct</h1>

```py
OpenStruct(self, fields={})
```

## init

Creates a new instance of an object, having fields with values which are defined
as an argument.

Fields can be declared by calling them on the left side of assignment.

```py
bob = OpenStruct()
bob.name = Bob
bob.age = 54
print(bob) # => [name=Bob, age=54]

su = OpenStruct({'name': 'Su', 'gender': 'female'})
su.employed = True
print(su) # => [name=Su, gender=female, employed=True]
```

## ==

Two instance are equivalent if both fields are equivalent.

## hash

Hash of an instance is based on the its fields and values.

## getattr

It gets executed when field is referenced on the instance.
If field is not declared before neither in ctor nor as a field, it returns
`None`.

```py
bob = OpenStruct()
bob.name = 'Bob'
print(bob.name)
```

## setattr

It gets executed when field is referenced on the instance and this reference is
on the left side of assignment.

## []

Provides support via keys for both reading and writing. Key is name of the
field.

```py
bob = OpenStruct()
bob['name'] = 'Bob'
bob['age'] = 50
print(bob.name, bob.age) # => Bob 50
```

## delete_field

Deletes given field.

```py
bob = OpenStruct({'name':'Bob', 'age': 30})
bob.delete_field('name')
print(bob) # => [age=30]
```

## each_pair

Returns list of pairs on which `callback` is applied.

```py
bob = OpenStruct({'name': 'Bob', 'age': 25})
bob.each_pair(lambda name, value: '{} {}'.format(name, value)) # => ['name Bob',
'age 25']
```

## to_dict

Returns the fieldnames and their values as a dict.


## str

Returns the string representation of the instance.






