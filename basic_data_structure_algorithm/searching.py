class Searching(object):

    def __init__(self):
        pass

    def linear_search(self, nums, seaching_key):
        """ Time Complexity:  O(n) & Auxiliary Space: O(1)"""
        for i in range(len(nums)):
            if nums[i] == seaching_key:
                return i
        return -1

    def binary_search(self, nums, seaching_key):
        """ Time Complexity:  O(log n) & Auxiliary Space: O(1)"""
        first = 0
        last = len(nums) - 1
        mid = 0
        while first <= last:
            mid = (first + last)//2
            if nums[mid] == seaching_key:
                return mid
            elif nums[mid] < seaching_key:
                first = mid+1
            else:
                last = mid-1
        return -1


# nums = [2, 3, 4, 2, 1, 1, 1, 2]
# seaching_key = 2
# searching = Searching()
# print(searching.linear_search(nums, seaching_key))
