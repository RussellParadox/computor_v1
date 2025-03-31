from monomial import Monomial

class Polynomial:
    def __init__(self, equation):
        compact_equation = equation.replace(' ', '')
        compact_equation = compact_equation.replace('-', '+-')

        equation_left, equation_right = compact_equation.split('=')
        self.monomials = [ Monomial(t) for t in equation_left.split('+') if t != '' ]
        self.monomials += [ Monomial('-' + t if t[0] != '-' else t[1:]) for t in equation_right.split('+') if t != '' ]

        self.reduce()
        self.degree = max(self.monomials, key=Monomial.degree_sort_key).degree

        self.solutions = None
        self.discriminant = 0
        match self.degree:
            case 0:
                if self.monomials[0].coefficient != 0:
                    self.solutions = []
            case 1 | 2 if self.getMonomial(2).coefficient == 0:
                a = self.getMonomial(1).coefficient
                b = self.getMonomial(0).coefficient
                if a != 0:
                    self.solutions = [-b / a]
                elif a == 0 and b != 0:
                    self.solutions = []
            case 2:
                a = self.getMonomial(2).coefficient
                b = self.getMonomial(1).coefficient
                c = self.getMonomial(0).coefficient
                self.discriminant = b ** 2 - 4 * a * c
                if self.discriminant < 0:
                    self.solutions = [
                        (-b - abs(self.discriminant ** 0.5) * 1j) / (2 * a),
                        (-b + abs(self.discriminant ** 0.5) * 1j) / (2 * a)
                    ]
                elif self.discriminant == 0:
                    self.solutions = [-b / (2 * a)]
                else:
                    self.solutions = [
                        (-b - self.discriminant ** 0.5) / (2 * a),
                        (-b + self.discriminant ** 0.5) / (2 * a)
                    ]

    def getMonomial(self, degree):
        return next((m for m in self.monomials if m.degree == degree), Monomial(f"0 * X^{degree}"))

    def reduce(self):
        self.monomials.sort(key=Monomial.degree_sort_key)
        reduced_monomials = []
        while len(self.monomials) > 0:
            degree = self.monomials[0].degree
            monomials = [ m for m in self.monomials if m.degree == degree ]
            reduced_monomials.append(sum(monomials, start=Monomial(f"0*X^{degree}")))
            self.monomials = [ m for m in self.monomials if m.degree != degree ]
        self.monomials = reduced_monomials

    def getReducedForm(self):
        reduced_form = f"{" ".join(map(str, self.monomials))} = 0"
        if reduced_form[0] == '-':
            return reduced_form[0] + reduced_form[2:]
        return reduced_form[2:]

    def getDegree(self):
        return self.degree

    def getDiscriminant(self):
        return self.discriminant

    def getSolutions(self):
        return self.solutions