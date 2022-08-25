class Solution(object):
    def reverse(self,nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left,right =left+1,right-1
        
        return nums
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        list_length = len(nums)
        nums = self.reverse(nums,0,list_length-1)
        k = k%list_length
        nums = self.reverse(nums,0,k-1)
        nums = self.reverse(nums,k,list_length-1)
        return nums