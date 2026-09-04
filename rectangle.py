"""Reference solution: Rectangle - Constructor and Equality.

Contains two implementations of the same concept:
- Rectangle:    "normal" class with manual constructor and __eq__
- RectangleDC:  dataclass with automatically generated constructor and __eq__
"""

class Rectangle:
    """Rectangle with width and height (classic implementation)."""

    def __init__(self, width: float = 1.0, height: float = 1.0) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than 0")
        self.width = width
        self.height = height

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.width == other.width and self.height == other.height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    @property
    def width(self):
        """ returns the width """
        return self._width

    @width.setter
    def width(self, value):
        """ sets the width """
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self._width = value

    @property
    def height(self):
        """ returns the height """
        return self._height

    @height.setter
    def height(self, value):
        """ sets the height """
        if value <= 0:
            raise ValueError("width and height must be greater than 0")
        self._height = value