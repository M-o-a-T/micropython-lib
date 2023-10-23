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
