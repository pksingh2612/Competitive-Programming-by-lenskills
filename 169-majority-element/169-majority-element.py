class Solution(object):
    def findMajorityElement(self, nums, n):
        maj_index = 0
        count = 1
        for i in range(n):
            if nums[maj_index] == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_index = i
                count = 1
        return nums[maj_index]
    
    def isMajority(self,nums,n,maj_element):
        count = 0
        for i in range(n):
            if nums[i] == maj_element:
                count += 1
        if count > n/2:
            return True
        else:
            return False
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_length = len(nums)
        ele = self.findMajorityElement(nums,list_length)
        
        if self.isMajority(nums, list_length, ele) == True:
            return ele
