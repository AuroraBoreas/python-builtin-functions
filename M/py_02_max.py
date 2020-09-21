import logging, random
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_max():
    """docs

    max(iterable, *[, key, default])
    max(arg1, arg2, *args[, key])
    """
    _lbound = 10
    _ubound = 100
    some_list = [
        random.randint(_lbound, _ubound)
        for _ in range(5)
    ]
    m = max(some_list)
    logging.debug(m)

    some_strings = [
        'hello world',
        '草泥马, 老天',
        'こにちは、世界',
        'bonjour toute le monde',
    ]
    
    r = max(some_strings, key=len)
    logging.debug(r)

if __name__ == "__main__":
    demo_max()