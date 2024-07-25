def apply_decorator_to_all_methods(cls, method):
    # function to add a decorator to all methods
    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)

        if callable(attr) and not attr_name.startswith("__"):
            setattr(cls, attr_name, method(attr))
    return cls
