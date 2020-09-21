import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class Cnm:
    pass

def demo_isinstance():
    c = Cnm()
    r = isinstance(c, Cnm)
    logging.debug(r)

if __name__ == "__main__":
    demo_isinstance()