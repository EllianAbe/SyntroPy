

def print_after_method(method):
    # decorator to print object after method
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        print('-' * 100)
        print('after', method.__name__)
        print(self)
        print('-' * 100)

        return result
    return wrapper
