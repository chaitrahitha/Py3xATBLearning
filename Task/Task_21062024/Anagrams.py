# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase
# String s1 = "silent"
# String s2 = "listen"
# namo - mano - onam

str = "silent"
str1 = "listen"
s1 = list(str)
s2 = list(str1)
s1.sort()
s2.sort()
if s1 == s2:
    print("Anagram")
else:
    print("Not Anagram")

