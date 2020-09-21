import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class MyClass:
    name = 'halo world'
    age  = 50_000

def demo_setattr():
    mc = MyClass()
    logging.debug(f'before setattr(), {mc.name}')
    setattr(mc, 'name', 'cnm')
    logging.debug(f'after setattr(), {mc.name}')

if __name__ == "__main__":
    demo_setattr()