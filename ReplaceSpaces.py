"""URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)
// EXAMPLE Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"
// use trim method and replace method in python"""

class ReplaceSpaces(object):
    def replacespaces(self, str):
        if len(str) <= 0: return str
        newstring = (str.strip(" ").replace(" ", "%20"))
        return newstring

r = ReplaceSpaces()
print(r.replacespaces("I am John Smith  "))