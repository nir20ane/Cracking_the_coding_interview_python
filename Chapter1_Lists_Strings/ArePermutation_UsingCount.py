"""Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
Count the characters in string and check if they are equal
Time complexity is O(n)
"""
class ArePermuttaion_UsingCount(object):
    def arepermutation_usingcount(self,str1,str2):
        if len(str1) != len(str2): return False
        count = [0]*128
        for char in str1:
            count[ord(char)] += 1
        for char in str2:
            count[ord(char)] -= 1
            if count[ord(char)] < 0: return False
        return True

a = ArePermuttaion_UsingCount()
print(a.arepermutation_usingcount("javacoding","codingjava"))
print(a.arepermutation_usingcount("javacoding","codingjave"))