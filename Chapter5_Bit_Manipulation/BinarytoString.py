"""
 * Given a real number between 0 and 1 (e.g., 0.72) that is passed
 * in as a double, print the binary representation. If the number
 * cannot be represented accurately in binary with at most 32
 * characters, print "ERROR".
"""
class BinaryString(object):
    def binstring(self, n):
        binstr = ""
        binstr += "."
        while n > 0:
            if n*2 >= 1:
                binstr += str(1)
                n = n*2-1
            else:
                n = n*2
                binstr += str(0)
        if len(binstr) > 32:
            raise Exception("ERROR MORE THAN 32 characters")
        return binstr

bin = BinaryString()
print(bin.binstring(0.75))
print(bin.binstring(0.5))
#print(bin.binstring(0.72))
