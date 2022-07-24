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
        count = 0
        for n in range(first,last):
            if n not in hash_set:
                count+=1
                nums.append(n)

        return [] if len(nums)+1==last else nums[-count:]