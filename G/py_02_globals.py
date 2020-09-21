import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_globals():
    logging.debug(globals())

if __name__ == "__main__":
    demo_globals()