class Monomial:
    def __init__(self, term: str):
        if '*' in term or 'X' not in term:
            self.coefficient = float(term.split('*')[0])
        else:
            self.coefficient = 1
        if '^' in term:
            try:
                self.degree = int(term.split('^')[-1])
                if self.degree < 0:
                    raise TypeError("Exponent need to be a whole integer.")
            except ValueError:
                raise TypeError("Exponent need to be a whole integer.")
        else:
            self.degree = 0

    def degree_sort_key(monomial):
        return monomial.degree

    def __add__(self, o):
        if self.degree == o.degree:
            return Monomial(f"{self.coefficient + o.coefficient}*X^{self.degree}")
        return Monomial("0*X^0")

    def __str__(self):
        if self.coefficient < 0 or self.coefficient is float(0):
            return f"- {f"{abs(self.coefficient)}".rstrip("0").rstrip(".")} * X^{self.degree}"
        return f"+ {f"{self.coefficient}".rstrip("0").rstrip(".")} * X^{self.degree}"