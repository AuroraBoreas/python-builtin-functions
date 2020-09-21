import logging, random
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_slice():
    _lbound = 10
    _ubound = 100
    some_list = [
        random.randint(_lbound, _ubound)
        for _ in range(5)
    ]
    logging.debug(f'before slice(), {some_list}')
    s = slice(1, 3)
    r = some_list[s]
    logging.debug(f'after slice(), {r}')

if __name__ == "__main__":
    demo_slice()