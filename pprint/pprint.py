import sys

import uio


def pformat(obj, indent=1, width=80, depth=None):
    buf = uio.StringIO()
    _pprint(obj, buf, indent, width, depth)
    return buf.getvalue()


def _pprint(obj, stream=None, indent=1, width=80, depth=None):
    if stream is None:
        stream = sys.stdout

    if isinstance(obj, dict):
        if not obj:
            stream.write("{}")
            return
        if len(obj) == 1:
            stream.write("{ ")
            for k, v in obj.items():
                _pprint(k, stream, indent + 1, width, depth)
                stream.write(": ")
                _pprint(v, stream, indent + 1, width, depth)
            stream.write(" }")
            return
        stream.write("{\n")
        for k, v in obj.items():
            stream.write("  " * indent)
            _pprint(k, stream, indent + 1, width, depth)
            stream.write(": ")
            _pprint(v, stream, indent + 1, width, depth)
            stream.write(",\n")
        stream.write("  " * indent + "}")
    elif isinstance(obj, (list, tuple)):
        if not obj:
            stream.write("[]" if isinstance(obj, list) else "()")
            return
        stream.write("[\n" if isinstance(obj, list) else "(\n")
        for v in obj:
            stream.write("  " * indent)
            _pprint(v, stream, indent + 1, width, depth)
            stream.write(",\n")
        stream.write("  " * indent + ("]" if isinstance(obj, list) else ")"))

    else:
        print(repr(obj), file=stream, end="")


def pprint(obj, stream=None, indent=1, width=80, depth=None):
    _pprint(obj, stream, indent, width, depth)
    print(file=stream)
