from monomial import Monomial

class Polynomial:
    def __init__(self, equation):
        compact_equation = equation.replace(' ', '')
        compact_equation = compact_equation.replace('-', '+-')

        equation_left, equation_right = compact_equation.split('=')
        self.monomials = [ Monomial(t) for t in equation_left.split('+') if t != '' ]
        self.monomials += [ Monomial('-' + t if t[0] != '-' else t[1:]) for t in equation_right.split('+') if t != '' ]

        self.reduce()
        self.solutions = None

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
        return max(self.monomials, key=Monomial.degree_sort_key).degree