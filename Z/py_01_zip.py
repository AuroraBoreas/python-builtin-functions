import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_zip():
    a = 'hello world'
    b = 'cnm keyima'
    r = zip(a, b)
    logging.debug(list(r))

if __name__ == "__main__":
    demo_zip()