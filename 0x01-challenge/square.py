#!/usr/bin/python3

class Square():
    """Representantion of a Square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialization of class object

        Args:
            args(tuple): non-key worded parameters.
            kwargs(dict): key-worded parameters.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of a Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representantion of Square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
