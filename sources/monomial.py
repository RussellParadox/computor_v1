class Monomial:
    def __init__(self, term):
        if '*' in term:
            self.coefficient = float(term.split('*')[0])
        elif 'X' in term:
            self.coefficient = 1
        else:
            self.coefficient = float(term)
        if '^' in term:
            self.degree = int(term.split('^')[-1])
        else:
            self.degree = 0