import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_reversed():
    import random
    _lbound = 10
    _ubound = 100
    some_ints = [
        random.randint(_lbound, _ubound)
        for _ in range(5)
    ]
    some_ints.sort()
    r = reversed(some_ints)
    logging.debug('before reversed: {}'.format(some_ints))
    logging.debug('after reversed : {}'.format(list(r)))

if __name__ == "__main__":
    demo_reversed()