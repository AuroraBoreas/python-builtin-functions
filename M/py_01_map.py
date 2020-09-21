import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')


def demo_map():
    a = range(5)
    r = map(lambda x: x**2, a)
    logging.debug(list(r))

if __name__ == "__main__":
    demo_map()