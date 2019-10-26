import pytest

from esu import OpenStruct

def test_init_openstruct_with_fields():
    dave = OpenStruct({'name': 'Dave', 'age': 25})
    assert dave['name'] == 'Dave' and dave['age'] == 25

def test_eq_openstruct_if_two_are_equivalent():
    dave = OpenStruct({'name': 'Dave', 'age': 25})
    double = OpenStruct({'name': 'Dave', 'age': 25})
    assert dave == double

def test_eq_openstruct_if_two_are_not_equivalent():
    dave = OpenStruct({'name': 'Dave', 'age': 25})
    anna = OpenStruct({'name': 'Anna', 'age': 23})
    assert dave != anna 

def test_eq_openstruct_if_other_is_different():
    dave = OpenStruct({'name': 'Dave', 'age': 25})
    assert dave != 12

def test_hash_openstruct_produce_different_keys():
    dave = OpenStruct({'name': 'Dave', 'age': 25})
    anna = OpenStruct({'name': 'Anna', 'age': 23})
    h = {}
    h[dave] = 1
    h[anna] = 2
    assert len(h) == 2

def test_hash_openstruct_produce_the_same_keys():
    dave = OpenStruct({'name': 'Dave', 'age': 25})
    anna = OpenStruct({'name': 'Dave', 'age': 25})
    h = {}
    h[dave] = 1
    h[anna] = 2
    assert len(h) == 1

def test_str_openstruct():
    dave = OpenStruct({'name': 'Dave', 'age': 25})
    assert 'name=Dave' in str(dave) and 'age=25' in str(dave)

def test_getattr_openstruct_name_exists():
    dave = OpenStruct({'name': 'Dave', 'age': 25})
    assert 'Dave' == dave.name

def test_getattr_openstruct_name_not_exists():
    dave = OpenStruct()
    assert None == dave.name

def test_setattr_openstruct():
    dave = OpenStruct()
    dave.name = 'Dave'
    assert 'Dave' == dave.name 

def test_getitem_openstruct_name_exists():
    dave = OpenStruct()
    dave['name'] = 'Dave'
    assert dave.name == 'Dave' 

def test_getitem_openstruct_name_not_exists():
    dave = OpenStruct()
    assert None == dave.name and None == dave['name']

def test_setitem_openstruct():
    dave = OpenStruct()
    dave['name'] = 'Dave'
    assert 'Dave' == dave.name and 'Dave' == dave['name']

def test_delete_field_openstruct_name_exists():
    dave = OpenStruct({'name': 'Dave', 'age':12})
    dave.delete_field('age')
    assert 'age=12' not in str(dave)
    
def test_delete_field_openstruct_name_not_exists():
    dave = OpenStruct({'name': 'Dave'})
    dave.delete_field('age')
    assert 'age=12' not in str(dave)

def test_each_pair_openstruct():
    dave = OpenStruct({'name': 'Dave', 'age':12})
    res = dave.each_pair(lambda name, value: (name, value))
    assert ('name', 'Dave') in res and ('age', 12) in res

def test_to_dict_openstruct():
    dave = OpenStruct({'name': 'Dave', 'age':12})
    assert dave.to_dict() == {'name': 'Dave', 'age':12}










