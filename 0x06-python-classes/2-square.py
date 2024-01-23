#!/usr/bin/python3
""" A Square class """


class Square:
    """ 
    Define the size of the Square 

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """ 
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except (TypeError, ValueError) as e:
            print(e)
