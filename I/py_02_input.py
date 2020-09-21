import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_input():
    # works in cmd/consol/terminal tho

    user_input = input('pls input an integer: ')
    logging.debug(user_input)

if __name__ == "__main__":
    demo_input()