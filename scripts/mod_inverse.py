# scripts/modular_inverse.py

INPUTS = [
    ("number", int),
    ("modulus", int),
]

def main(args: dict) -> str:
    number = args["number"]
    modulus = args["modulus"]
    
    if number % modulus == 0:
        raise ValueError("Modular inverse does not exist when number is divisible by modulus")
    
    inverse = pow(number, -1, modulus)
    
    return f"modular_inverse : {inverse}"
