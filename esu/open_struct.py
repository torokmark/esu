import copy


class OpenStruct(object):
    def __init__(self, fields={}):
        self.__dict__["fields"] = copy.deepcopy(fields)
        for field in fields:
            self.__dict__["fields"][field] = fields[field]

    def __eq__(self, other):
        if not isinstance(other, OpenStruct):
            return False
        for name in self.__dict__["fields"]:
            if self.__dict__["fields"].get(name) != other.__dict__["fields"].get(name):
                return False
        else:
            return True

    def __hash__(self):
        s = (
            "["
            + ", ".join(
                "{}={}".format(field, self.__dict__["fields"].get(field))
                for field in self.__dict__["fields"]
            )
            + "]"
        )
        return hash(s)

    def __getattr__(self, name):
        return self.__dict__["fields"].get(name)

    def __setattr__(self, name, value):
        self.__dict__["fields"][name] = value

    def __getitem__(self, name):
        return self.__dict__["fields"].get(name)

    def __setitem__(self, name, value):
        self.__dict__["fields"][name] = value

    def delete_field(self, name):
        if name in self.__dict__["fields"]:
            del self.__dict__["fields"][name]

    def each_pair(self, callback):
        _list = []
        for name, value in self.__dict__["fields"].items():
            _list.append(callback(name, value))
        return _list

    def to_dict(self):
        return {
            field: self.__dict__["fields"].get(field)
            for field in self.__dict__["fields"]
        }

    def __str__(self):
        s = (
            "["
            + ", ".join(
                "{}={}".format(field, self.__dict__["fields"].get(field))
                for field in self.__dict__["fields"]
            )
            + "]"
        )
        return s
