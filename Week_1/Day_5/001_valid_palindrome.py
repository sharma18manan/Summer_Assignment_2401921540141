class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new=""
        for ch in s:
            if ch.isalnum():
                new=new+ch
        if(new[::-1]==new):
            return True
        else:
            return False