class utils:
    """Utility class with helper functions for number manipulation."""
    
    @staticmethod
    def reversed(number):
        """
        Reverses a number.
        
        Args:
            number (int): The number to reverse.
            
        Returns:
            int: The reversed number.
        """
        if not isinstance(number, int):
            raise TypeError(f"Expected int, got {type(number).__name__}")
        
        is_negative = number < 0
        reversed_num = int(str(abs(number))[::-1])
        
        return -reversed_num if is_negative else reversed_num
    
    @staticmethod
    def formatter(number):
        """
        Formats a number in binary and octal representation.
        
        Args:
            number (int): The number to format.
            
        Returns:
            dict: A dictionary with 'binary' and 'octal' keys containing the formatted strings.
        """
        if not isinstance(number, int):
            raise TypeError(f"Expected int, got {type(number).__name__}")
        
        binary = bin(number)  # Returns format like '0b101'
        octal = oct(number)   # Returns format like '0o5'
        
        return {
            'binary': binary,
            'octal': octal
        }
