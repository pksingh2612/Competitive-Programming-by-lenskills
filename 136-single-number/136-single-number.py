class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        if 1<=len(nums)<=3*10**4:
            for num in nums:
                if -3*10**4 <= num <= 3*10**4:
                    result = result ^ num
        return result
        