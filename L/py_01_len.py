import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_len():
    a = "Exercitation excepteur nostrud incididunt est."
    logging.debug(len(a))

if __name__ == "__main__":
    demo_len()