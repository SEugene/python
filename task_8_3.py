from functools import wraps


def type_logger(func):
    @wraps(func)
    def type_wrapper(*args, **kwargs):
        calc = func(*args, **kwargs)

        return {arg: type(arg) for arg in args}, {'The result of function is: ': calc}, func

    return type_wrapper


@type_logger
def calc_cube(x, y=3):
    return x ** y


print(calc_cube(5, 4))
print(calc_cube(5))
print(calc_cube(5.2, 4))
print(calc_cube(6.8))
