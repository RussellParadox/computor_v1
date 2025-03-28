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

        self.reduce()

        print()
        for m in self.monomials:
            print("Coefficient: ", m.coefficient, ", Degree: ", m.degree)

        print(f"Reduced form: {self.getReducedForm()}")
        print(f"Polynomial degree: {self.getDegree()}")
    
    def reduce(self):
        self.monomials.sort(key=Monomial.degree_sort_key)
        i = 0
        while i < len(self.monomials) - 1:
            if self.monomials[i].degree == self.monomials[i+1].degree:
                monomials_sum = self.monomials[i] + self.monomials[i+1]
                self.monomials[i] = monomials_sum
                del self.monomials[i+1]
            i+=1

    def getReducedForm(self):
        reduced_form = f"{" ".join(map(str, self.monomials))} = 0"
        if reduced_form[0] == '-':
            return reduced_form[0] + reduced_form[2:]
        return reduced_form[2:]

    def getDegree(self):
        return max(self.monomials, key=Monomial.degree_sort_key).degree

    def printAnswer(self):
        pass