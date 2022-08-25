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
    
    def isMajority(self,nums,n,maj_element1,maj_element2):
        count1 = 0
        count2 = 0
        for i in range(n):
            if nums[i] == maj_element1:
                count1 += 1
            elif nums[i] == maj_element2:
                count2 += 1
        # print(count1,count2,n/3)
        
        if count1 > n/3 and count2 > n/3:
            return True,True
        elif count1 > n/3 and count2 <= n/3:
            return True,False
        elif count1 <= n/3 and count2 > n/3:
            return False,True
        else:
            return False,False
            
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_length = len(nums)
        ele1,ele2 = self.findTwoMajorityElement(nums,list_length)
        # print(ele1,ele2)
        ele1R,ele2R = self.isMajority(nums, list_length, ele1, ele2)
        # print(ele1R,ele2R)
        if  ele1R == True and ele2R == True:
            return [ele1,ele2]
        elif ele1R == True and ele2R == False:
            return [ele1]
        elif ele1R == False and ele2R == True:
            return [ele2]
        