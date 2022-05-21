class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        next=n-1
        return True if n&next == 0 and n!=0 else False