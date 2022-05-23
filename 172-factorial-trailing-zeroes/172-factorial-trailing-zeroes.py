class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        i=5
        while (i<=n):
            res = res + n//i
            i=i*5
        return res