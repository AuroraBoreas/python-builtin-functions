import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_open():
    with open(__file__, 'r') as f:
        data = f.read()
    logging.debug(data)

if __name__ == "__main__":
    demo_open()