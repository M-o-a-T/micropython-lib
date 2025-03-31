"""
Typing support. We don't have that.

Thus this code works with CPython checkers but has minimal impact on MicroPython:

    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from typing import whatever, you, need

    def foo() -> whatever:
        ...
"""
TYPE_CHECKING = const(False)

# Stubs we need inline

def assert_type(val, typ):
    return val

def cast(typ, val):
    return val

def no_type_check(fn):
    return fn

def overload(fn):
    return fn

def override(fn):
    return fn
