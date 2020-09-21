import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')


def demo_chr():
    s = [34, 65, 89]
    for i in s:
        r = chr(i)
        logging.debug(r)

if __name__ == "__main__":
    demo_chr()