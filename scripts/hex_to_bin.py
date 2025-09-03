INPUTS = [("hex_number", str)]

def main(args):
    if not args:
        print("Usage: input.txt should have 1 hex value after 'hex_to_bin'")
        return
    hex_num = args[0]
    try:
        bin_val = bin(int(hex_num, 16))[2:]
        print(f"Binary of {hex_num} = {bin_val}")
    except ValueError:
        print("Invalid hex value")
