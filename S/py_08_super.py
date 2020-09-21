import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class A:
    pass

class B(A):
    def __init__(self, *args):
        super().__init__()
        self.args = args
    def __repr__(self):
        return 'B({})'.format(self.args)


def demo_super():
    mc = B(1, 2, 3)
    logging.debug(mc)

if __name__ == "__main__":
    demo_super()