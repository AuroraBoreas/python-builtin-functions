import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_hasattr():
    import math
    r = hasattr(math, 'inf')
    logging.debug(r)

if __name__ == "__main__":
    demo_hasattr()