INPUTS = [
    ("hex", str),
    ("dec", int),
    ("bin", str),
]

def main(args):
    if "hex" in args and args["hex"] is not None:
        value = int(args["hex"], 16)
        return (
            f"dec : {value}\n"
            f"bin : {bin(value)[2:]}"
        )
    elif "dec" in args and args["dec"] is not None:
        value = int(args["dec"])
        return (
            f"hex : {hex(value).upper().replace('X', 'x')}\n"
            f"bin : {bin(value)[2:]}"
        )
    elif "bin" in args and args["bin"] is not None:
        value = int(args["bin"], 2)
        return (
            f"dec : {value}\n"
            f"hex : {hex(value).upper().replace('X', 'x')}"
        )
    else:
        raise ValueError("Provide one of 'hex', 'dec', or 'bin' as input.")
