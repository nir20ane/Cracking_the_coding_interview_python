""" Problem:Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
Time complexity: O(n)
Space Complexity: O(1) or 128, as we create an array of 128 boolean valuesQuestion to ask is array and ASCII array """

class IsUnique(object):
    def IsUnique(self,s):
        if len(s) > 128: return False
        char_set = [False for _ in range(128)]
        for char in s:
            val = ord(char)
            if char_set[val]: return False
            char_set[val] = True
        return True

u = IsUnique()
print(u.IsUnique("string"))
print(u.IsUnique("python"))
print(u.IsUnique("unique"))
