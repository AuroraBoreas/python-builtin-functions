import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_tuple():
    a = 'hello world'
    t = tuple(a)
    logging.debug(t)

if __name__ == "__main__":
    demo_tuple()