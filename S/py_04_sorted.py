import logging, random
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_sorted():
    _lbound = 10
    _ubound = 100
    some_list = [
        random.randint(_lbound, _ubound)
        for _ in range(5)
    ]
    r = sorted(some_list, reverse=True)
    logging.debug(r)

if __name__ == "__main__":
    demo_sorted()