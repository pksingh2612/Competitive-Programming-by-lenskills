class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t=[0,1,1]
        for i in range(0,n+1):
            t.append(t[i]+t[i+1]+t[i+2])
            
        
        return t[n]