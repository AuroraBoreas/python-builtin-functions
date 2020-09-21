import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_int():
    """docs
    
    class int([x])
    lass int(x, base=10)
    """
    some_string = '10'
    r = int(some_string)
    logging.debug(r)

    some_binary = b'1111'
    r = int(some_binary, base=2)
    logging.debug(r) # should be 15

if __name__ == "__main__":
    demo_int()