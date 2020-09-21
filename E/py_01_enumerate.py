import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_enumerate():
    some_list = range(10)
    for i, j in enumerate(some_list, start=1):
        logging.debug(f'i={i:>2}, j={j:<2}')

if __name__ == "__main__":
    demo_enumerate()