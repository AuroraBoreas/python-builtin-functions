import random
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_divmod():
    _lbound = 10
    _ubound = 100
    a = random.randint(_lbound, _ubound)
    b = random.randint(_lbound, _ubound)
    r = divmod(a, b)
    logging.debug(f'{a} divmod {b} = {r}')

if __name__ == "__main__":
    demo_divmod()