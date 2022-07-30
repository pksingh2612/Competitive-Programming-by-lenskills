class Solution:
    def sortColors(self, nums):
        left=0
        curr=0
        right=len(nums)-1
        
        while left<=right:
            if nums[left]==0:
                nums[left],nums[curr]=nums[curr],nums[left]
                left+=1
                curr+=1
            elif nums[left]==2:
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
            else:
                left+=1