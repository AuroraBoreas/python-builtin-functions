import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_oct():
    a = 10
    r = oct(a)
    logging.debug(r)

if __name__ == "__main__":
    demo_oct()