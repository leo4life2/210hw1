class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ZeroDivisionError()

    def gcf(a, b):
        # Euclid's algorithm
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b / gcf(a, b)

    def __add__(self, other):
        """
        create and return a new Fraction object, which is the sum of self + other.
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the sum of self + other.
        """
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __iadd__(self, other):
        """
        modify the self Fraction object, which adds other Fraction object value to self.

        :param other: Fraction -- the other fraction number.
        :return: self. The value of self should become the sum of self + other.
        """
        self.numerator *= other.denominator
        self.numerator += other.numerator * self.denominator
        return self

    def __sub__(self, other):
        """
        create and return a new Fraction object, which is the subtraction of self - other.
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the subtraction of self - other.
        """
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        """
        create and return a new Fraction object, which is the multiplication of self * other.
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the multiplication of self * other.
        """
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __eq__(self, other):
        """
        Compare if self Fraction object has equal numerical value to the other Fraction object.
        Example: 2/3 == 4/6 --> True
                 2/3 == 2/3 --> True
        If you use the reduce() function here, it is fine.

        :param other: Fraction -- the other fraction number.

        :return: True if the float value of self is equal to other;
                 False if the float value of self is not equal to other.
        """
        self.reduce()
        other.reduce()
        return self.numerator == other.numerator and self.denominator == other.denominator

    def reduce(self):
        """
        Reduces (Simpilifies) the self Fraction object.
        Modifies both self.numerator and self.denominator.
        For example: 12 / 24 --> 1 / 2;  16 / 20 --> 4 / 5

        :return: Nothing.
        """
        gcf = Fraction.gcf(self.numerator, self.denominator)

        self.numerator //= gcf
        self.denominator //= gcf

    def __str__(self):
        """
        Displays the self Fraction object nicely.
        Recommended format:
        Suppose,
        self.numerator = 5
        self.denominator = 6
        Then, should return "5 / 6"

        :return: The string representation of self Fraction object.
        """
        return f"{self.numerator} / {self.denominator}"



'''
Note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

# def main():
#     x = Fraction(3, 4)
#     y = Fraction(4, 6)
#     print(x)        # 3 / 4
#     print(y)        # 4 / 6
#     print(x + y)    # 34 / 24 or any value that is equal
#     z = x + y
#     print(x * y)    # 12 / 24 or any value that is equal
#     print(x - y)    # 2 / 24 or any value that is equal
#     y.reduce()
#     print(y)        # 2 / 3
#     z.reduce()
#     print(z)        # 17 / 12
#
#     print(z == Fraction(-17, -12))  # True
#     print(z == Fraction(51, 36))  # True
#     print(z == Fraction(-7, 4))   # False
#
# if __name__ == '__main__':
#     main()
