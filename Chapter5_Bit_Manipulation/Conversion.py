"""* Conversion: Write a function to determine the number of bits you would need to flip to convert
* integer A to integer B.
* EXAMPLE
* Input:
* Output:
* SOLUTION
* 29 (or: 11101), 15 (or: 01111)
* 2
*"""
class Conversion(object):
    def conversion(self,x, y):
        diff = x^y
        count = 0
        while diff != 0:
            diff = diff&(diff-1)
            count += 1
        return count

conv = Conversion()
print(conv.conversion(29, 15))
