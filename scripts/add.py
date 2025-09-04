INPUTS = [("a", int), ("b", int)]

def main(args):
    try:
        a = int(args["a"])
        b = int(args["b"])
    except KeyError:
        return "Missing arguments: a, b"
    return a + b
