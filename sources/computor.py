import argparse

from polynomial import Polynomial

parser = argparse.ArgumentParser()
parser.add_argument("equation", type=str, help="A polynomial equation.")

def printAnswer(self):
    print(f"Reduced form: {self.getReducedForm()}")
    if self.solutions is not None:
        print(f"Polynomial degree: {self.getDegree()}")

if __name__ == "__main__":
    args = parser.parse_args()
    equation = args.equation

    polynomial = Polynomial(equation)
    printAnswer()
