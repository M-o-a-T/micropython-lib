import sys


def _pprint(obj, stream, indent=0, spc=""):
    if isinstance(obj, dict):
        stream.write(spc+"{\n")
        for k, v in obj.items():
            stream.write("  "*indent)
            _pprint(k, stream, indent+1)
            stream.write(": ")
            _pprint(v, stream, indent+1)
            stream.write(",\n")
        stream.write("  "*indent+"}")
        return

    if isinstance(obj, (list,tuple)):
        se = "[]" if isinstance(obj,list) else "()"
        stream.write(spc+se[0]+"\n")
        for k in obj:
            stream.write("  "*indent)
            _pprint(k, stream, indent+1, spc="  ")
            stream.write(",\n")
        stream.write("  "*indent+se[1])
        return

    print(repr(obj), file=stream, end="")


def pformat(obj):
    import io
    buf = io.StringIO()
    _pprint(obj, buf)
    return buf.getvalue()

def pprint(obj, stream=sys.stdout):
    _pprint(obj, stream)
    stream.write("\n")
