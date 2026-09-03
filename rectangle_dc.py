from dataclasses import dataclass, field


@dataclass
class RectangleDC:
    """Rectangle with width and height (dataclass implementation).

    @dataclass automatically generates the constructor and __eq__ based on
    the declared attributes. A custom __eq__ method is therefore not
    needed - the generated comparison checks class and all attributes.
    """

    width: float = field(default=1.0)
    height: float = field(default=1.0)

    def __post_init__(self) -> None:
        print (f"RectangleDC created with width={self.width} and height={self.height}")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("width and height must be greater than 0")

    @property
    def width(self):
        """ returns the width """
        return self._width

    @width.setter
    def width(self, value):
        """ sets the width """
        self._width = value

    @property
    def height(self):
        """ returns the height """
        return self._height
    
    @height.setter
    def height(self, value):
        """ sets the height """
        self._height = value