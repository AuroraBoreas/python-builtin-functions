import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_frozenset():
    """docs

    set() vs frozenset()

    A set object is an unordered collection of distinct hashable objects. 
    The set type is mutable — the contents can be changed using methods like add() and remove(). 
    The frozenset type is immutable and hashable — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.
    
    """
    text = 'abcdefgaaaaaaa'
    s = set(text)
    fs = frozenset('abcdefgaaaaaaa')
    logging.debug(s)
    s.add('x')
    hash(s) # exception
    logging.debug(fs)
    hash(fs) # pass
    
if __name__ == "__main__":
    demo_frozenset()