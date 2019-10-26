import copy


class Struct:
    def __new__(self, cls, *fields, methods={}):
        NewType = type(cls, (object,), {field: None for field in fields})

        def __init__(c, *values):
            if len(values) == len(fields):
                for idx in range(len(fields)):
                    c.__dict__[fields[idx]] = values[idx]
            elif len(values) != 0:
                raise ValueError("Not enough arguments passed")

        setattr(NewType, "__init__", __init__)

        def __eq__(c, obj):
            for field in fields:
                if c.__dict__.get(field) != obj.__dict__.get(field):
                    return False
            return True

        setattr(NewType, "__eq__", __eq__)

        def __hash__(c):
            s = (
                "["
                + ", ".join(
                    ["{}={}".format(field, c.__dict__.get(field)) for field in fields]
                )
                + "]"
            )
            return hash(s)

        setattr(NewType, "__hash__", __hash__)

        def __str__(c):
            return (
                "["
                + ", ".join(
                    ["{}={}".format(field, c.__dict__.get(field)) for field in fields]
                )
                + "]"
            )

        setattr(NewType, "__str__", __str__)

        def members(c):
            return copy.deepcopy(fields)

        setattr(NewType, "members", members)

        def values(c):
            _values = []
            for field in fields:
                _values.append(c.__dict__[field])
            return tuple(_values)

        setattr(NewType, "values", values)

        def __len__(c):
            return len(fields)

        setattr(NewType, "__len__", __len__)

        def to_dict(c):
            _dict = {}
            for field in fields:
                _dict[field] = c.__dict__[field]
            return _dict

        setattr(NewType, "to_dict", to_dict)

        for method_name, method in methods.items():
            setattr(NewType, method_name, method)

        return NewType
