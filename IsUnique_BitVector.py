""" Problem:Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
Time complexity: O(n)
Space Complexity: O(1) or 128, as we create an array of 128 boolean valuesQuestion to ask is array and ASCII array """

class IsUnique_BitVector(object):
    def IsUnique(self,s):
        if len(s) > 128: return False
        checker = 0
        for char in s:
            val = ord(char) - ord('a')
            newval = 1<<val
            if (checker & newval) > 0: return False
            checker |= newval
        return True

u = IsUnique_BitVector()
print(u.IsUnique("string"))
print(u.IsUnique("python"))
print(u.IsUnique("unique"))
