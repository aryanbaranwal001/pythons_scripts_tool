# scripts/bin_to_hex.py
INPUTS = [("binary", str)]

def main(args):
    try:
        s = str(args["binary"]).strip()
    except KeyError:
        return "Missing argument: binary"

    # normalize: allow '0b' prefix, spaces, and underscores
    s = s.lower()
    if s.startswith("0b"):
        s = s[2:]
    s = s.replace(" ", "").replace("_", "")

    if not s:
        return "Invalid binary string"
    if any(c not in "01" for c in s):
        return "Invalid binary string"

    try:
        value = int(s, 2)
    except ValueError:
        return "Invalid binary string"

    # Hexadecimal with 0x prefix (uppercase)
    return f"0x{value:X}"
