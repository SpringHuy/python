"""
    keypress - detecting a single key press.
"""

try:
    import msvcrt

    def getkey():
        """
            wait for a keypress and return a single character string
        """
        return msvcrt.getch()
except ImportError :
    import sys
    import tty
    import termios
    def getkey():
        """
            wait for a keypress and return a single character string
        """
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr()
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch