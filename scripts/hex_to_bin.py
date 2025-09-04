INPUTS = [("hex", str)]

def main(args: dict) -> str:
    hex_val = args["hex"]
    if not hex_val.lower().startswith("0x"):
        raise ValueError("Hex value must start with 0x")
    try:
        return bin(int(hex_val, 16))[2:]
    except ValueError:
        raise ValueError("Invalid hexadecimal input")
