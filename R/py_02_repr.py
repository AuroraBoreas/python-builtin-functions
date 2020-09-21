import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_repr():
    o = object()
    some_str = repr(o)
    logging.debug(some_str)
    
if __name__ == "__main__":
    demo_repr()