#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Class Square:
    Attributes:
        size(int) : sier of the square.
        x (int): the x coordination.
        y (int): the y coordination.
        id (int): id.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Init a square obj"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value
    
