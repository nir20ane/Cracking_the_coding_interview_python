"""** 1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another.
* Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")

** Approach: Concatenate str1+str1 and check for str2 in the concatenated string
* Time Complexity - O(n^2)
* Space Complexity - O(1)

*/"""

class StringRotation(object):
    def stringRotation(self, A, B):
        return len(A) == len(B) and B in A+A

strrot = StringRotation()
print(strrot.stringRotation("bata", "taba"))
print(strrot.stringRotation("bata", "tabe"))
