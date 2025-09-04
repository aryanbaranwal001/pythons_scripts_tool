INPUTS = [("n", int)]

def main(args):
    try:
        n = int(args["n"])
    except KeyError:
        return "Missing argument: n"
    except ValueError:
        return "n must be an integer"

    if n < 0:
        return "Error: Factorial of negative number not defined"

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
