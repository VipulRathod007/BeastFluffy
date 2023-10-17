""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" @file operations._OPCopy.py                                                                                      """
""" Contains the definition of Copy class                                                                            """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# To access non-exposed modules
from operations._IOperable import Ops, IOperable


class Copy(IOperable):
    """
    Represents class for Copy Operations
    """

    def __init__(self, inValue):
        super(Copy, self).__init__(inValue)
        self.parse(inValue)

    @property
    def Identifier(self):
        """
        Class property
        :return: The Identifier of the class
        """
        return Ops.COPY

    def parse(self, inValue):
        """
        In-class definition to parse the operation arguments
        :param inValue: The operation arguments
        """
        # TODO: Parsing logic here
        pass
