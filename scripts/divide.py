INPUTS = [("numerator", float), ("denominator", float)]

def main(args):
    try:
        num = float(args["numerator"])
        den = float(args["denominator"])
    except KeyError:
        return "Missing arguments: numerator, denominator"

    if den == 0:
        return "Error: Division by zero"
    return num / den
