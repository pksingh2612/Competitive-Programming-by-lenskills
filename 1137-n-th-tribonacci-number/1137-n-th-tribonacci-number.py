class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        second = 1
        third = 1
        if 0<=n<=1:
            return n
        if n==2:
            return third
        for i in range(3,n+1):
            curr = first + second + third
            first = second
            second = third
            third = curr
        return third