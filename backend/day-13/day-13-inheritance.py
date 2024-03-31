class BasicCalculator:
    def sum(self, numlist: list):
        _sum = 0
        for num in numlist:
            _sum += num
        return _sum

class ComplexCalculator(BasicCalculator):  
    @staticmethod
    def power(base, exponent):  
        return base ** exponent

    @staticmethod
    def abs(number):  
        if number >= 0:
            return number
        return -number

basic = BasicCalculator()
complex = ComplexCalculator()

print(basic.sum([1, 2, 3]))
print(complex.sum([1, 2, 3]))  
