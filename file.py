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
    def collect_keys(func):
        def check_keys(*args):
            input_dict = func(*args)
            output_dict = dict()
            for required_key in required_keys:
                if required_key in input_dict:
                    if value := input_dict[required_key]:
                        output_dict[required_key] = value
                    else:
                        output_dict[required_key] = "Empty value"
                else:
                    split_keys = required_key.split('__')
                    tmp = list()
                    for split_key in split_keys:
                        if split_key in input_dict:
                            if value := input_dict[split_key]:
                                tmp.append(value)
                            else:
                                tmp.append("Empty value")
                        else:
                            raise ValueError
                    output_dict[required_key] = " ".join(tmp)

            return output_dict

        return check_keys

    return collect_keys


def add_method_to_instance(klass):
    def collect_klass(func):
        def func_as_method(*args):
            return func()
        setattr(klass, func.__name__, func_as_method)
        return func
    return collect_klass

