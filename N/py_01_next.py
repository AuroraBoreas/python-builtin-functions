import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_next():
    some_str = "je m'en fou complétement"
    r = iter(some_str)
    for _ in range(len(some_str)):
        logging.debug(next(r))


if __name__ == "__main__":
    demo_next()