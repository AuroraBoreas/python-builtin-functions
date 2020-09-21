import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')


def demo_hash():
    a  = '10'
    b  = '10'
    ha = hash(a)
    hb = hash(b)
    logging.debug(ha)
    logging.debug(hb)

if __name__ == "__main__":
    demo_hash()