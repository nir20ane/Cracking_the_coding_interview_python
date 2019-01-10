"""One Away: There are three types of edits that can be performed on strings: insert a character,
* remove a character, or replace a character. Given two strings, write a function to check if they are
* one edit (or zero edits) away.
* EXAMPLE
* pale, ple -> true
* pales, pale -> true
* pale, bale -> true
* pale, bae -> false
* Approach - increase count if there is a mismatch in character or length
* increase index 1 if string1 length is more and index 2 if string 2 length is more
* Time Complexity O(n); Space Complexity O(1)
"""
class OneEditString(object):
    def oneEditString(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        index1 = 0
        index2 = 0
        count  = 0
        if(abs(len1-len2) > 1): return False
        while((index1 < len1) & (index2 < len2)):
            if(str1[index1] != str2[index2]):
                if(count == 1):
                    return False
                if(len1 < len2): index2 += 1
                elif(len1 > len2): index1 += 1
                else:
                    index1 += 1
                    index2 += 1
                count += 1
            else:
                index1 += 1
                index2 += 1
        if((index1 < len1) | (index2 < len2)): count += 1
        return count == 1

one = OneEditString()
print(one.oneEditString("pale", "bale"))
print(one.oneEditString("ale", "bale"))
print(one.oneEditString("pale", "balee"))
print(one.oneEditString("ale", "ale"))
print(one.oneEditString("ble", "pale"))
print(one.oneEditString("ble", "paleeeee"))


