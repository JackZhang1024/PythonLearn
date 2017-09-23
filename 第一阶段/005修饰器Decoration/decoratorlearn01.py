# -*- coding:utf-8 -*-


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s() ' % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            func(*args, **kw)
        return wrapper
    return decorator


# @log
@log('test')
def now(name='zhang', *args, **kwargs):
    print('2017-03-01')

now('jack')

