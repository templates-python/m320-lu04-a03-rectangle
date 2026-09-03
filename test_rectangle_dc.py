"""PyTest tests for rectangle_dc.py (constructor and equality)."""
import pytest

from rectangle import Rectangle
from rectangle_dc import RectangleDC


class TestRectangleDCConstructor:
    def test_default_values_dc(self):
        r = RectangleDC()
        assert r.width == 1.0
        assert r.height == 1.0

    def test_values_assigned_dc(self):
        r = RectangleDC(3, 4)
        assert r.width == 3
        assert r.height == 4

    def test_invalid_width_raises_value_error_dc(self):
        with pytest.raises(ValueError):
            RectangleDC(0, 4)

    def test_invalid_height_raises_value_error_dc(self):
        with pytest.raises(ValueError):
            RectangleDC(3, -1)


class TestRectangleDCEquality:
    def test_equal_content_is_equal_dc(self):
        assert RectangleDC(3, 4) == RectangleDC(3, 4)

    def test_different_content_is_not_equal_dc(self):
        assert RectangleDC(3, 4) != RectangleDC(3, 5)

    def test_identity_vs_equality_dc(self):
        r1 = RectangleDC(3, 4)
        r2 = r1
        r3 = RectangleDC(3, 4)

        assert r1 is r2
        assert r1 == r2
        assert r1 is not r3
        assert r1 == r3


def test_rectangle_and_rectangledc_are_never_equal():
    """Different classes are never considered equal, even if
    width and height match."""
    assert Rectangle(3, 4) != RectangleDC(3, 4)