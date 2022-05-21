class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(0,len(nums)+1,1):
        #     if i not in nums:
        #         return i
        n = len(nums)
        sum_of_natural_number = (n*(n+1))//2
        sum_of_nums = sum(nums)
        total = (sum_of_natural_number - sum_of_nums)
        return total