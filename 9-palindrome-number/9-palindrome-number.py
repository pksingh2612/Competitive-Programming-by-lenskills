class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        res = 0
        temp = x
        bool_res = False
        while temp>0:
            rem = temp%10
            res = res*10 + rem
            temp = temp//10
        if res == x:
            bool_res = True
        return bool_res