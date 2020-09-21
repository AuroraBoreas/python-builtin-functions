import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class MyClass:
    def __init__(self, *args):
        self.args = args
    def __len__(self):
        return len(self.args)
    def __repr__(self):
        return 'MyClass({})'.format(self.args)
    def __dir__(self):
        return ['args']

def demo_dir():
    """docs
    Without arguments, return the list of names in the current local scope.
    With an argument, attempt to return a list of valid attributes for that object.
    """
    r = dir()
    logging.debug(r)
    mc = MyClass()
    r = dir(mc)
    logging.debug(r)

if __name__ == "__main__":
    demo_dir()