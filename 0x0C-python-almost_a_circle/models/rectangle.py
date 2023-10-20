#!/usr/bin/python3
"""define rectangle class"""
from models.base import Base

class Rectangle(Base):
    """rep rectangle class
        Args:
            width (int): The width of Rectangle.
            height (int): The height of Rectangle.
        
        Attributes:
            __width: represents the private att
            __height: rep private att
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle that inherits from base class.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the Rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y coordinate of the Rectangle."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of a Rectangle"""
        return self.__width * self.__height
    
    def display(self):
        """display the rectagle using the #"""
        if self.height == 0 or self.width ==0:
            print('')
            return

        [print("") for y in range(self.y)]
        for index in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """print() and str() repr of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)
    

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) >= 1 and args[0] is not None:
                self.id = args[0]
            else:
                self.id
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)