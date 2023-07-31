def isPalindrome(s, left,right):
    if left > right:
        return True
    if s[left] == s[right]:
        return isPalindrome(s, left+1, right-1)
    else:
        return False
    

s = 'racecar'
print(isPalindrome(s, 0, len(s) - 1))