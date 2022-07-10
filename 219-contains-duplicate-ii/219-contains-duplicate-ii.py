class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in hash_map and abs(i-hash_map[num])<=k:
                return True
            hash_map[num]=i
        return False