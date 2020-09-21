import logging, random
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_pow():
    _lbound = 1
    _ubound = 10
    a = random.randint(_lbound, _ubound)
    b = random.randint(_lbound, _ubound)
    r = pow(a, b)
    logging.debug(f'pow({a},{b}) = {r}')

if __name__ == "__main__":
    demo_pow()