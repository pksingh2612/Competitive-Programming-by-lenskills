class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """ Time Complexity:  O(nlogn) & Auxiliary Space: O(sort)"""
        ans = []
        for c in nums:
            nums[abs(c)-1] = -abs(nums[abs(c)-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans