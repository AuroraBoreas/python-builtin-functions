import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_bytes():
    """docs
    
    Return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256. 
    bytes is an immutable version of bytearray – it has the same non-mutating methods 
    and the same indexing and slicing behavior.

    Accordingly, constructor arguments are interpreted as for bytearray().

    Bytes objects can also be created with literals, see String and Bytes literals.
    """
    a = 'a'
    r = bytes(a, encoding='utf-8')
    logging.debug(r)

if __name__ == "__main__":
    demo_bytes()