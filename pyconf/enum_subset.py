from collections import OrderedDict
from enum import Enum

from typing import Type, List

from pyconf.enum_utils import str_to_enum_value


class EnumSubset(object):
    def __init__(self, enum_type, list_of_values):
        # type: (Type[Enum], List[Type[Enum]]) -> None
        self.enum_type = enum_type
        self.selected = OrderedDict()
        for value in list_of_values:
            self.add(value)

    def add(self, enum_value):
        assert enum_value in enum_value.__class__.__members__.values(), "bad value {}".format(enum_value)
        self.selected[enum_value] = None

    def delete(self, enum_value):
        del self.selected[enum_value]

    def yield_values(self):
        for value in self.selected.keys():
            yield value

    def __contains__(self, item):
        return item in self.selected

    def has_value(self, item):
        return item in {x.value for x in self.selected}

    @classmethod
    def from_string(cls, e, s):
        # type: (Type[Enum], str) -> EnumSubset
        r = EnumSubset(enum_type=e, list_of_values=[])
        for name in s.split(','):
            v = str_to_enum_value(s=name, e=e)
            r.add(v)
        return r

    def list_of_strings(self):
        my_list = []
        for x in self.selected:
            my_list.append(x.name)
        return my_list

    def to_string(self):
        return ",".join(self.list_of_strings())

