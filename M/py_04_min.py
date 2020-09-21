import logging, random
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_min():
    """docs

    min(iterable, *[, key, default])
    min(arg1, arg2, *args[, key])
    """

    _lbound = 10
    _ubound = 100
    some_ints = [
        random.randint(_lbound, _ubound)
        for _ in range(5)
    ]
    r = min(some_ints)
    logging.debug(r)

    some_strings = [
        'hello world',
        '草泥马, 老天',
        'こにちは、世界',
        'bonjour toute le monde',
    ]
    r = min(some_strings, key=len)
    logging.debug(r)


if __name__ == "__main__":
    demo_min()