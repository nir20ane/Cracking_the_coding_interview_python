"""
 * Write a program to swap odd and even bits in an integer with
 * as few instructions as possible (e.g., bit 0 and bit 1 are
 * swapped, bit 2 and bit 3 are swapped, and so on).
"""
class SwapOddEvenBits(object):
    def swap(self, n):
        evenbits = n & 0xAAAAAAAA
        oddbits = n & 0x55555555
        evenshift = evenbits >> 1
        oddshift = oddbits << 1
        return evenshift | oddshift

swp = SwapOddEvenBits()
print(swp.swap(23))  #23 = 00010111, 43 = 00101011
