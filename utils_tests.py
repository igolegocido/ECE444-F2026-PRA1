import pytest
from utils import utils


class TestReversed:
    """Test cases for the reversed function."""
    
    def test_reversed_with_positive_integer(self):
        """Test reversed function with a positive integer."""
        assert utils.reversed(12345) == 54321
    
    def test_reversed_with_negative_integer(self):
        """Test reversed function with a negative integer."""
        assert utils.reversed(-12345) == -54321
    
    def test_reversed_with_zero(self):
        """Test reversed function with zero."""
        assert utils.reversed(0) == 0
    
    def test_reversed_with_string_raises_error(self):
        """Test reversed function with string input raises TypeError."""
        with pytest.raises(TypeError):
            utils.reversed("12345")
    
    def test_reversed_with_float_raises_error(self):
        """Test reversed function with float input raises TypeError."""
        with pytest.raises(TypeError):
            utils.reversed(123.45)
    
    def test_reversed_with_single_digit(self):
        """Test reversed function with single digit integer."""
        assert utils.reversed(5) == 5


class TestFormatter:
    """Test cases for the formatter function."""
    
    def test_formatter_with_positive_integer(self):
        """Test formatter function with a positive integer."""
        result = utils.formatter(10)
        assert result['binary'] == '0b1010'
        assert result['octal'] == '0o12'
    
    def test_formatter_with_zero(self):
        """Test formatter function with zero."""
        result = utils.formatter(0)
        assert result['binary'] == '0b0'
        assert result['octal'] == '0o0'
    
    def test_formatter_with_negative_integer(self):
        """Test formatter function with a negative integer."""
        result = utils.formatter(-10)
        assert result['binary'] == '-0b1010'
        assert result['octal'] == '-0o12'
    
    def test_formatter_with_string_raises_error(self):
        """Test formatter function with string input raises TypeError."""
        with pytest.raises(TypeError):
            utils.formatter("42")
    
    def test_formatter_with_float_raises_error(self):
        """Test formatter function with float input raises TypeError."""
        with pytest.raises(TypeError):
            utils.formatter(42.5)
    
    def test_formatter_with_large_number(self):
        """Test formatter function with a large number."""
        result = utils.formatter(255)
        assert result['binary'] == '0b11111111'
        assert result['octal'] == '0o377'
