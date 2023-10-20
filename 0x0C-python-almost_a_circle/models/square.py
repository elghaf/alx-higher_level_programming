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

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init a square obj"""
        super().__init__(width, height, x, y, id)