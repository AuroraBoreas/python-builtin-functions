import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class MyClass:
    name = 'cnm world'
    age  = '50000'
    sex  = 'unknown'

def demo_getattr():
    attrs = [
        'name',
        'age',
        'sex',
    ]
    for attr in attrs:
        logging.debug(getattr(MyClass, attr))

    # builtin pkg
    import operator
    logging.debug(getattr(operator, 'abs'))

if __name__ == "__main__":
    demo_getattr()