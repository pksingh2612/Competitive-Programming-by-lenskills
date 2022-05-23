class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        temp = x
        res = False
        while temp>0:
            rem = temp%10
            rev = rev*10 + rem
            temp = temp//10
        if rev == x:
            res = True
        return res