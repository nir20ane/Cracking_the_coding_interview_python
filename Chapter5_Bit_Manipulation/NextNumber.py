"""
 * Next Number: Given a positive integer, print the next smallest and the next largest number
 * that have the same number of 1 bits in their binary representation.
"""
class NextNumber(object):
    def countones(self, n):
        count = 0
        while n != 0:
            n &= (n - 1)
            count += 1
        return count

    def nexttnum(self, x):
        ones = self.countones(x)
        while x < (2**31):
            x = x+1
            if self.countones(x) == ones:
                return x
        return -1

    def beforenum(self, x):
        ones = self.countones(x)
        while x!= 0:
            x = x-1
            if self.countones(x) == ones:
                return x
        return -1


nextnum = NextNumber()
print(nextnum.beforenum(5))
print(nextnum.nexttnum(5))
print(nextnum.beforenum(50))
print(nextnum.nexttnum(50))
