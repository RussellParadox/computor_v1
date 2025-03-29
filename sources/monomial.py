class Monomial:
    def __init__(self, term: str):
        if '*' in term or 'X' not in term:
            self.coefficient = float(term.split('*')[0])
        else:
            self.coefficient = 1
        if '^' in term:
            self.degree = int(term.split('^')[-1])
        else:
            self.degree = 0

    def degree_sort_key(monomial):
        return monomial.degree

    def __add__(self, o):
        if self.degree == o.degree:
            return Monomial(f"{self.coefficient + o.coefficient}*X^{self.degree}")
        return Monomial("0*X^0")

    def __str__(self):
        if self.coefficient <= 0:
            return f"- {abs(self.coefficient)} * X^{self.degree}"
        return f"+ {self.coefficient} * X^{self.degree}"