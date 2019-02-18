"""*
* Flip Bit to Win: You have an integer and you can flip exactly one bit from a O to a 1.
* Write code to find the length of the longest sequence of 1 s you could create.
* EXAMPLE
* Input: 1775
* Output: 8
* SOLUTION (or: 11011101111)
* """
class FlipBitstoWin(object):
    def flip(self, n):
        if ~n == 0:
            return len(bin(n))
        previouslength = 0
        currentlength = 0
        maxlength = 1
        while n != 0:
            if n&1 == 1:
                currentlength += 1
                print currentlength
            elif n & 1 == 0:
                if n & 2 == 0:
                    previouslength = 0
                else:
                    previouslength = currentlength
                    currentlength = 0
            maxlength = max(previouslength+currentlength+1, maxlength)
            n >>= 1
            print(bin(n))
        return maxlength

flibits = FlipBitstoWin()
print(flibits.flip(1775))
