import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class MyClass:
    def __init__(self):
        pass
    @staticmethod
    def display():
        ...

def demo_staticmethod():
    mc = MyClass()
    logging.debug(mc.display())

if __name__ == "__main__":
    demo_staticmethod()