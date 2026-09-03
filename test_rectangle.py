"""PyTest tests for rectangle.py (constructor and equality)."""
import pytest

from rectangle import Rectangle


class TestRectangleConstructor:
    def test_default_values(self):
        r = Rectangle()
        assert r.width == 1.0
        assert r.height == 1.0

    def test_values_assigned(self):
        r = Rectangle(3, 4)
        assert r.width == 3
        assert r.height == 4

    def test_invalid_width_raises_value_error(self):
        with pytest.raises(ValueError):
            Rectangle(0, 4)

    def test_invalid_height_raises_value_error(self):
        with pytest.raises(ValueError):
            Rectangle(3, -1)


class TestRectangleEquality:
    def test_equal_content_is_equal(self):
        assert Rectangle(3, 4) == Rectangle(3, 4)

    def test_different_content_is_not_equal(self):
        assert Rectangle(3, 4) != Rectangle(3, 5)

    def test_identity_vs_equality(self):
        r1 = Rectangle(3, 4)
        r2 = r1
        r3 = Rectangle(3, 4)

        assert r1 is r2          # same reference
        assert r1 == r2          # therefore also equal in content
        assert r1 is not r3      # different objects
        assert r1 == r3          # but equal in content

    def test_comparison_with_other_type(self):
        r = Rectangle(3, 4)
        assert r != "not a rectangle"
        assert r != (3, 4)
        assert r != 42