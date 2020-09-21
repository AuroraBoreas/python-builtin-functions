import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_set():
    a = 'hello world'
    s = set(a)
    logging.debug(s)

if __name__ == "__main__":
    demo_set()