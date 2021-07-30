"""
    A module for dealing with BMP bitmap image files.
"""

def write_grayscale(filename, pixels):
    """
    Create and writes a grayscale BMP file.

    Args:
        filename: Name of the BMP file to be created
        pixels: A rectangular image stored as a sequence of rows. 
            Each row must be an iterable series of integers in the range 0-255.

        Raises: 
            VallueError: If any of the intger values are out of range.
            OSError: If the file couldn't be written.
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        #BMP header
        bmp.write(b'BM')
        size_bookmark = bmp.tell()      # The next four bytes hols the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for now.

        bmp.write(b'\x00\x00')      #Unused 16-bit integer - shouble be zero
        bmp.write(b'\x00\x00')      #Unused 16-bit integer - shouble be zero

        pixels_offset_bookmark = bmp.tell()     # 4 bytes - integer offset to the pixel data. Zero place holder for now
        bmp.write(b'\x00\x00\x00\x00') 

        #Image Header
        bmp.write(b'\x28\x00\x00\x00')      #Image header sixe in bytes - 40 decimal
        bmp.write(_int32_to_bytes(width))   #Image width in pixels
        bmp.write(_int32_to_bytes(height))  #Image height in pixels
        bmp.write(b'\x01\x00')              #Number if image planes
        bmp.write(b'\x08\x00')              #Bit per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00')      #No copression
        bmp.write(b'\x00\x00\x00\x00')      #Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')      #Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')      #Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')      #Use whole color table
        bmp.write(b'\x00\x00\x00\x00')      #All colors are important

        # Color paletter - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c,c,c,0)))     #Blue, Green, Red, Zero
        
        #Pixel data
        pixels_data_bookmark = bmp.tell()
        for row in reversed(pixels):        #BMP files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * ((4-(len(row)%4)) % 4)      # pad row to multiple o ffour bytes
            bmp.write(padding)
        
        #End of file
        eof_bookmark = bmp.tell()

        # Fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in pixel
        bmp.seek(pixels_offset_bookmark)
        bmp.write(_int32_to_bytes(pixels_data_bookmark))


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


def dimensions(filename):
    """Determine the dimensions in pixels of a BMP image.
    Args:
        filename: The filename of a BMP file.
    Returns:
        A tuple containing two integer with the width
        and height in pixels.
    Raises:
        ValueError: If the file was not aBMP file.
        OSError: If there was a problem reading the file.
    """
    with open(filename, 'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))

        f.seek(18)
        width_bytes = f.read(4)
        height_bytes = f.read(4)

        return (_bytes_to_int32(width_bytes),
                _bytes_to_int32(height_bytes))


def _bytes_to_int32(b):
    return b[0] | (b[1] << 8) | (b[2] << 16 | (b[3] << 24))


### how to run
# https://github.com/kentoj/python-fundamentals/blob/master/fractal.py
"""
import IO_fractal
pixels = IO_fractal.mandelbrot(448, 256)
import reprlib
reprlib.repr(pixels)
import IO_BMP_writer
IO_BMP_writer.write_grayscale("mandel.bmp", pixels)
"""