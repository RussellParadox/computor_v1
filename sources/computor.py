import argparse

from polynomial import Polynomial

parser = argparse.ArgumentParser()
parser.add_argument("equation", type=str, help="A polynomial equation.")

if __name__ == "__main__":
    args = parser.parse_args()
    equation = args.equation

    polynomial = Polynomial(equation)
    polynomial.printAnswer()
