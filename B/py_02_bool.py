import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_bool():
    some_shit = [
        '',
        ' ',
        0,
        1,
        [],
        (),
        {},
    ]

    for i in some_shit:
        r = bool(i)
        logging.debug('bool({!r:^3}) = {}'.format(i, r))

if __name__ == "__main__":
    demo_bool()