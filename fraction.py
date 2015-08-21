class Fraction:

    def __init__(self, numerator, denominator):
        if type(numerator) != int or type(denominator) != int:
            raise RuntimeError('NUMERATOR AND DENOMINATOR MUST BE INTEGERS')
        if denominator == 0:
            raise RuntimeError('CANNOT DIVIDE BY ZERO')

        if denominator < 0 and numerator > 0:
            numerator = -1 * numerator

        this_gcd = gcd(numerator, denominator)

        self.numerator = numerator // this_gcd
        self.denominator = denominator // this_gcd

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def show(self):
        print(self.numerator, '/', self.denominator)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __repr__(self):
        repr_string = 'Fraction({}, {})'
        repr_string = repr_string.format(self.numerator, self.denominator)
        return repr_string

    def __add__(self, other):
        numerator = (self.numerator * other.denominator +
                         self.denominator * other.numerator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = (self.numerator * other.denominator -
                         self.denominator * other.numerator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        first_number = self.numerator * other.denominator
        second_number = self.denominator * other.numerator
        return first_number == second_number

    def __le__(self, other):
        first_number = self.numerator * other.denominator
        second_number = self.denominator * other.numerator
        return first_number <= second_number

    def __lt__(self, other):
        first_number = self.numerator * other.denominator
        second_number = self.denominator * other.numerator
        return first_number < second_number

def gcd(m, n):
    while m % n != 0:
        m_previous = m
        n_previous = n

        m = n_previous
        n = m_previous % n_previous
    return n

if __name__ == '__main__':
    a = Fraction(100, 5)
    b = Fraction(-4, -5)
    print('{} + {} = {}'.format(a, b, a + b))
    print('{} - {} = {}'.format(a, b, a - b))
    print('{} * {} = {}'.format(a, b, a * b))
    print('{} / {} = {}'.format(a, b, a / b))
    print('{} > {} = {}'.format(a, b, a > b))
    print('{} < {} = {}'.format(a, b, a < b))
    print('{} >= {} = {}'.format(a, b, a >= b))
    print('{} <= {} = {}'.format(a, b, a <= b))
    print('{} == {} = {}'.format(a, b, a == b))
    print('{} != {} = {}'.format(a, b, a != b))
    print('{} += {}'.format(a, b), end=' ')
    a += b
    print('{}'.format(a))
    print()

    a = Fraction(-31, 7)
    b = Fraction(160, -29)
    print('{} + {} = {}'.format(a, b, a + b))
    print('{} - {} = {}'.format(a, b, a - b))
    print('{} * {} = {}'.format(a, b, a * b))
    print('{} / {} = {}'.format(a, b, a / b))
    print('{} > {} = {}'.format(a, b, a > b))
    print('{} < {} = {}'.format(a, b, a < b))
    print('{} >= {} = {}'.format(a, b, a >= b))
    print('{} <= {} = {}'.format(a, b, a <= b))
    print('{} == {} = {}'.format(a, b, a == b))
    print('{} != {} = {}'.format(a, b, a != b))
    print('{} += {}'.format(a, b), end=' ')
    a += b
    print('{}'.format(a))
    print()

    try:
        print('Fraction(1.0, 2.0)')
        Fraction(1.0, 2.0)
    except RuntimeError as e:
        print('\t{}'.format(e))

    try:
        print('Fraction(1, 0)')
        Fraction(1, 0)
    except RuntimeError as e:
        print('\t{}'.format(e))

    print(a.__str__())
    print(a.__repr__())
