import random
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_abs():
    a = random.randint(1, 100) * -1
    b = abs(a)
    logging.debug(b)

if __name__ == "__main__":
    demo_abs()