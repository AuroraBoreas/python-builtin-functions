import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_exec():
    program = 'a = 5\nb= 10\nprint("sum = ", a + b)'
    r = exec(program)
    logging.debug(r)

if __name__ == "__main__":
    demo_exec()