import argparse

from polynomial import Polynomial

parser = argparse.ArgumentParser()
parser.add_argument("equation", type=str, help="A polynomial equation.")

def printAnswer(polynomial):
    solutions = polynomial.getSolutions()
    degree = polynomial.getDegree()
    discriminant = polynomial.getDiscriminant()

    print(f"Reduced form: {polynomial.getReducedForm()}")
    if degree > 2:
        print(f"Polynomial degree: {degree}")
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    elif solutions is None:
        print("Any real number is a solution.")
    elif not solutions:
        print("No solution.")
    elif degree == 1:
        print(f"The solution is:\n{round(solutions[0], 6)}")
    elif degree == 2:
        print(f"Polynomial degree: {degree}")
        if discriminant < 0:
            print(f"Discriminant is strictly negative, the two complex solutions are:\n{round(solutions[0].real, 6)} + {abs(round(solutions[0].imag, 6))}i\n{round(solutions[1].real, 6)} - {abs(round(solutions[1].imag, 6))}i")
        elif discriminant == 0:
            print(f"Discriminant is zero, the solution is:\n{round(solutions[0], 6)}")
        else:
            print(f"Discriminant is strictly positive, the two solutions are:\n{round(solutions[0], 6)}\n{round(solutions[1], 6)}")

    print()

if __name__ == "__main__":
    args = parser.parse_args()
    equation = args.equation

    try:
        polynomial = Polynomial(equation)
        printAnswer(polynomial)
    except TypeError as e:
        print(e)
