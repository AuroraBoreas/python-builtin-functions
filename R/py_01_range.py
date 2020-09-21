import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_range():
    some_ints = range(1, 10)
    for i in some_ints:
        logging.debug(i)

if __name__ == "__main__":
    demo_range()