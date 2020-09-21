import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def greating(name: str) -> None:
    logging.debug(f'hello {name}')

class MyClass:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def __str__(self):
        return 'MyClass({}, {})'.format(self.args, self.kwargs)


def demo_format():
    """docs

    str.format()
    format()
    """
    mc = MyClass(1, 2, 3, hello='world', toute='monde')
    logging.debug(mc)

    some_list = [
        format('helloworld', '<25'),
        format(10, 'b'),
        format(10, 'x'),
        format(10, 'o'),
        format(10, 'E'),
    ] 
    for i in some_list:
        logging.debug(i)


if __name__ == "__main__":
    demo_format()