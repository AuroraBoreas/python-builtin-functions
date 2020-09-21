import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_print():
    """docs

    io.flush() mechnism tho
    """
    import sys, time
    some_list = [
        i for i in range(5)
    ]
    print('test 01: print(), default args')
    for i in some_list:
        time.sleep(1)
        print(i)
    print("test 02: print(), end=' '")
    for i in some_list:
        time.sleep(1)
        # sys.stdout.flush()
        print(i, end=' ')
    print('\ntest 03: added sys.stdout.flush()')
    for i in some_list:
        time.sleep(1)
        sys.stdout.flush()
        print(i, end=' ')

if __name__ == "__main__":
    demo_print()