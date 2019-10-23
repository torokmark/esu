
class Struct:
    def __new__(self, cls, *names, methods={}):
        NewType = type(cls, (object,), {name : None for name in names})
        def __eq__(c, obj):
            for name in names:
                print('==>', name)
                if c.__dict__.get(name) != obj.__dict__.get(name):
                    return False
            return True
        setattr(NewType, '__eq__', __eq__)
       
        def __hash__(c):
            s = '[' + ', '.join(['{}={}'.format(name, c.__dict__.get(name)) for name in names]) + ']'
            return hash(s)
        setattr(NewType, '__hash__', __hash__)

        def __str__(c):
            return '[' + ', '.join(['{}={}'.format(name, c.__dict__.get(name)) for name in names]) + ']'
        setattr(NewType, '__str__', __str__)

        for method_name, method in methods.items():
            setattr(NewType, method_name, method)
        
        return NewType


