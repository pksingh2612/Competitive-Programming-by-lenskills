class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        N = (high-low)>>1 # divide by 2 => right shift
        
        if high&1 == 1 or low&1 == 1: # hight % 2 or high&1  same
            N+=1

        return N