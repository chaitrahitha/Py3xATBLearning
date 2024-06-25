#Palindrome String

def isPalindrome(s):
    # Code here
    rev = s[::-1]
    if rev == s:
        return True
    else:
        return False

print(isPalindrome("naman"))
print(isPalindrome("nitin"))
print(isPalindrome("level"))
print(isPalindrome("pramod"))
print(isPalindrome("Hello"))
print(isPalindrome("racecar"))
print(isPalindrome("madam"))
# i/p = naman , nitin, level
# o/p = true

# i/p = pramod
# o/p = false