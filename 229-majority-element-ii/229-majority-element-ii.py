class Solution(object):
    def findTwoMajorityElement(self, nums, n):
        maj_index1 = -1
        maj_index2 = -1
        count1 = 0
        count2 = 0
        for i in range(n):
            if nums[maj_index1] == nums[i]:
                count1 += 1
            elif nums[maj_index2] == nums[i]:
                count2 += 1
            elif count1 == 0:
                maj_index1 = i
                count1 += 1
            elif count2 == 0:
                maj_index2 = i
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        return nums[maj_index1],nums[maj_index2]
            
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_length = len(nums)
        maj_element1,maj_element2 = self.findTwoMajorityElement(nums,list_length)
        count1 = 0
        count2 = 0
        for i in range(list_length):
            if nums[i] == maj_element1:
                count1 += 1
            elif nums[i] == maj_element2:
                count2 += 1
        cond = list_length/3
        if count1 > cond and count2 > cond:
            return [maj_element1,maj_element2]
        elif count1 > cond and count2 <= cond:
            return [maj_element1]
        elif count1 <= cond and count2 > cond:
            return [maj_element2]
        else:
            return []
        