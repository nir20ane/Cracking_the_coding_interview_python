"""** 1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another.
* Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")

** Approach: Use two loops, inner loop should not increment when characters mismatch
* Time Complexity - O(n^2)
* Space Complexity - O(1)

*/"""

class StringRotation(object):
    def stringRotation(self, A, B):
        if len(A) != len(B): return False  # return false for length mismatch
        if len(A) == 0: return True  # return true if length is 0
        n = len(A)
        for s in range(n):
                if all(A[(s+i)%n] == B[i] for i in range(n)):  #logic to keep iterator going
                    return True
        return False

strrot = StringRotation()
print(strrot.stringRotation("bata", "taba"))
print(strrot.stringRotation("bata", "tabe"))

