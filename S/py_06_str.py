import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_str():
    """docs

    class str(object='')
    class str(object=b'', encoding='utf-8', errors='strict')
    """
    x = 10
    r = str(x)
    logging.debug(r)
    y = "草泥马"
    r = str(y, encoding='utf-16')
    logging.debug(r)

if __name__ == "__main__":
    demo_str()