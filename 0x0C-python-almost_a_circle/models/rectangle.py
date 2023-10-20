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
