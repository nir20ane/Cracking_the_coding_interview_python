import re
import string

frequency = {}
document_text = open('/Users/nirranjhane/Downloads/test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\bpattern\b', text_string)
print match_pattern
for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

#for word in frequency.keys():
    #print word, frequency[word]