def greeter(func):
    def inner(*args):
        string = func(*args)
        modified = f"Aloha {string.title()}"
        return modified
    return inner


def sums_of_str_elements_are_equal(func):
    def inner(*args):
        string = func(*args)
        numbers = string.split(' ')
        result = list()
        for number in numbers:
            if number[0] == '-':
                result.append(-sum([int(digit) for digit in number[1:]]))
            else:
                result.append(sum([int(digit) for digit in number]))
        if result[0] == result[1]:
            sign = '=='
        else:
            sign = '!='
        return f"{result[0]} {sign} {result[1]}"
    return inner


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
