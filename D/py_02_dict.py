import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_dict():
    """docs

    class dict(**kwarg)
    class dict(mapping, **kwarg)
    class dict(iterable, **kwarg)

    NOTE: how to construct a dict?
    """
    d1 = dict(zip('abcde', range(4)))
    d2 = dict(
        a=1,
        b=2,
        c=3
    )
    mykwargs = [
        (1, 'a'),
        (2, 'b'),
        (3, 'c'),
    ]
    d3 = dict(mykwargs)
    logging.debug(d1)
    logging.debug(d2)
    logging.debug(d3)

if __name__ == "__main__":
    demo_dict()