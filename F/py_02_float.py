import logging
logging.basicConfig(level=logging.DEBUG,format='(%(asctime)s) %(message)s')

def demo_float():
    """docs

    arg format
    
    sign            ::= "+" | "-"
    infinity        ::= "Infinity" | "Inf"
    nan             ::= "nan"
    numeric_value   ::= floatnumber | infinity | nan
    numeric_string  ::= [sign] numeric_value
    
    """
    some_strings = [
        '-3.1415',
        '+2.718\n',
        '-Infinity',
        'nan',
    ]
    for i in some_strings:
        r = float(i)
        logging.debug(r)

if __name__ == "__main__":
    demo_float()