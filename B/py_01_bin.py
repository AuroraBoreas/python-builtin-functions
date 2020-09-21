import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_bin():
    a: int = 7
    b: int = 9
    bin_a = bin(a)
    bin_b = bin(b)
    bin_r = bin(a | b)
    int_r = int(bin_r, base=2)
    logging.debug(f'{bin_a} | {bin_b} = {bin_r}, {int_r}')

if __name__ == "__main__":
    demo_bin()
