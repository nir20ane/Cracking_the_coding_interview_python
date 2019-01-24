"""** 1.6 String Compression: Implement a method to perform basic string compression using the counts
* of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
* "compressed" string would not become smaller than the original string, your method should return
* the original string. You can assume the string has only uppercase and lowercase letters (a - z).
* Approach: use Lists, calc compressed length, return orginal string if compressed length is longer
* Time Complexity O(n); Space Complexity O(n)d
*/"""

class StringCompreswsion(object):
    def compress(self, s1):
        finallength = self.calclen(s1)  # calculate compressed string length
        if(finallength >= len(s1)): return s1 # if compressed length is longer, return original string
        comlst = []
        countcons = 0
        for i in range(0, len(s1)):
            countcons += 1
            if(((i+1) >= len(s1)) or (s1[i] != s1[i+1])):  # check for end of string and character mis match
                comlst.append(s1[i])
                comlst.append(str(countcons))  # then append character and count
                countcons = 0
        return "".join(comlst)  # convert list to string

    def calclen(self, str):
        countcons = 0
        complen = 0
        for i in range(0, len(str)):
            countcons += 1
            if((i == (len(str)-1)) or (str[i+1] != str[i])): # check for end of string and character mis match
                complen += 2  # then increment compressed length by 2 every time
                countcons = 0
        return complen  # return compressed length


sc = StringCompreswsion()
print(sc.compress("aaaggff"))
print(sc.compress("aaaggkkssgyykkggddhbnhffcgg"))
print(sc.compress("a"))
print(sc.compress("abc"))
