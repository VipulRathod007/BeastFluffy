""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" @file operations._IOperable.py                                                                                   """
""" Contains the definition of IOperable class                                                                       """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


from abc import ABC, abstractmethod
from enum import IntEnum


class Ops(IntEnum):
    """
    Represents Enum class for supported Operations
    """
    COPY            = 0
    MOVE            = 1
    NOTSUPPORTED    = -1

    @classmethod
    def __contains__(cls, inValue: str) -> int:
        if inValue.upper() in cls._member_map_:
            return cls._member_map_[inValue.upper()].value
        else:
            return cls.NOTSUPPORTED

    def __str__(self):
        return self.name


class IOperable(ABC):
    """
    Represents abstract class for Operations
    """

    def __init__(self, inValue):
        self.parse(inValue)

    @property
    @abstractmethod
    def Identifier(self):
        """
        Class property
        :return: The Identifier of the class
        """
        pass

    @abstractmethod
    def parse(self, inValue):
        """
        In-class definition to parse the operation arguments
        :param inValue: The operation arguments
        """
        pass
