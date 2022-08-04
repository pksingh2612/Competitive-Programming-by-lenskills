class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        N = (high-low)//2
        
        if high&1 == 1 or low&1 == 1:
            N+=1

        return N