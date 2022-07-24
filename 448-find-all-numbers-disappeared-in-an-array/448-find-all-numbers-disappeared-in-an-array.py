class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """ Time Complexity:  O(nlogn) & Auxiliary Space: O(sort)"""
        hash_set = set(nums)
        first = 1
        last = len(nums) + 1
        result = []
        for n in range(first,last):
            if n not in hash_set:
                result.append(n)
        return result