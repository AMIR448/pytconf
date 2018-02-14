from enum import Enum

from pytconf.enum_subset import EnumSubset


class ExtendedEnum(Enum):

    @classmethod
    def get_list_of_all_values(cls):
        return [x for x in cls.__members__.values()]

    @classmethod
    def get_enum_subset_all(cls):
        return EnumSubset(
            enum_type=cls.__class__,
            list_of_values=cls.get_list_of_all_values()
        )