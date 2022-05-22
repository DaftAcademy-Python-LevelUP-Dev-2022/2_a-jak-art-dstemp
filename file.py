def greeter(func):
    def inner(*args):
        string = func(*args)
        modified = f"Aloha {string.title()}"
        return modified
    return inner


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
