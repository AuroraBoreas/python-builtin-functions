import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_round():
    a = 3.1415926
    r = round(a, 2)
    logging.debug(r)

if __name__ == "__main__":
    demo_round()