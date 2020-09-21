import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_complex():
    a = complex('1+2j')
    b = complex('1 + 2j')
    logging.debug(a)
    logging.debug(b) # exception

if __name__ == "__main__":
    demo_complex()