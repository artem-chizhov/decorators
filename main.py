from decorator import logger

@logger(path='logs', log_name='test2.log')
def test_func(x1, x2=0, x3=2):
    return x1+x2*x3

if __name__ == '__main__':
    test_func(x1=222, x2=23135)