from monomial import Monomial

class Polynomial:
    def __init__(self, equation):
        compact_equation = equation.replace(' ', '')
        compact_equation = compact_equation.replace('-', '+-')

        equation_left, equation_right = compact_equation.split('=')
        self.monomials = [ Monomial(t) for t in equation_left.split('+') if t != '']
        self.monomials += [ Monomial('-' + t if t[0] != '-' else t[1:]) for t in equation_right.split('+') if t != '']

        for m in self.monomials:
            print("Coefficient: ", m.coefficient, ", Degree: ", m.degree)

    def printAnswer(self):
        pass