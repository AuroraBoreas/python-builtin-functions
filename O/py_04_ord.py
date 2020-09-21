import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_ord():
    some_string = '草泥马'
    for i in some_string:
        logging.debug(ord(i))

if __name__ == "__main__":
    demo_ord()