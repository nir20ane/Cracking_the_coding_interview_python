"""
 * You are given two 32-bit numbers, N and M, and two bit positions,
 * i and j. Write a method to insert M into N such that M starts at
 * bit j and ends at bit i. You can assume that the bits j through i
 * have enough space to fit all of M. That is, if M = 10011, you can
 * assume that there are at least 5 bits between j and i. You would
 * not, for example, have j = 3 and i = 2, because M could not fully
 * fit between bit 3 and bit 2.
 *
 * EXAMPLE
 * Input: N = 10000000000, M = 10011, i = 2, j = 6
 * Output: N = 10001001100
 *
 * Key:
 * First create mask 11110000011 on N, then place M into N.
"""
class Insertion(object):
    def insertion(self, n , m, i , j):
        # create all 1s
        allones = ~0
        print bin(allones)

        # create left side
        left = allones << (j+1)
        print bin(left)

        # create right side
        right = (1 << i) - 1
        print bin(right)

        # create mask
        mask = left | right
        print bin(mask)

        # clear between i and j
        ncleared = n & mask
        print bin(ncleared)

        # shift m by i places
        mshifted = m << i
        print bin(mshifted)

        # set the bits between i and j in n, with m
        updated = mshifted | ncleared
        print bin(updated)

        # return updated value
        return updated

inst = Insertion()
inst.insertion(1024, 19, 2, 6)
