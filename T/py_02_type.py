import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_type():
    a = 'hello world'
    s = type(a)
    logging.debug(s)

if __name__ == "__main__":
    demo_type()