
class Struct:
    def __new__(self, cls, *fields, methods={}):
        NewType = type(cls, (object,), {field : None for field in fields})
        def __eq__(c, obj):
            for field in fields:
                if c.__dict__.get(field) != obj.__dict__.get(field):
                    return False
            return True
        setattr(NewType, '__eq__', __eq__)
       
        def __hash__(c):
            s = '[' + ', '.join(['{}={}'.format(field, c.__dict__.get(field)) for field in fields]) + ']'
            return hash(s)
        setattr(NewType, '__hash__', __hash__)

        def __str__(c):
            return '[' + ', '.join(['{}={}'.format(field, c.__dict__.get(field)) for field in fields]) + ']'
        setattr(NewType, '__str__', __str__)

        for method_name, method in methods.items():
            setattr(NewType, method_name, method)
        
        return NewType


