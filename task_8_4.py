def val_checker(value):
    def _checker(func):
        def type_wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for el in args:
                if el <= 0:
                    raise ValueError(f'wrong value of the argument: {el}')
            return res

        return type_wrapper

    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x, y):
    return x ** 3, y ** 3


print(calc_cube(5, 3))
