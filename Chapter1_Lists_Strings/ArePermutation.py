"""Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
Sort each string and check if they are equal
Time complexity is O(nlogn) as we have done sorting
"""

class ArePermutation(object):
    def arepermutation(self,str1, str2):
        if len(str1) != len(str2): return False
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False

a = ArePermutation()
print(a.arepermutation("pythoncoding","codingpython"))
print(a.arepermutation("pythoncoding","codingpythoe"))


