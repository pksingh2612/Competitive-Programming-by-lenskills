class Sorting(object):

    def __init__(self):
        pass

    def selection_sort(self,nums):
        # Traverse through all array elements
        nums_length = len(nums)
        for num in range(nums_length):
            # Find the minimum element in remaining
            # unsorted array
            minimum_index = num
            second_minimum_index = num + 1
            for num_next in range(second_minimum_index, nums_length):
                if nums[minimum_index] > nums[num_next]:
                    minimum_index = num_next
            # Swap the found minimum element with
            # the first element
            nums[num], nums[minimum_index] = nums[minimum_index], nums[num]

        return nums

    def bubble_sort(self,nums):
        # Traverse through all array elements
        nums_length = len(nums)
        for i in range(nums_length):
            swapped = False
            # Last i elements are already in place
            for j in range(0, nums_length-i-1):
                # traverse the array from 0 to n-i-1. Swap if the element found is greater than the next element
                if nums[j] > nums[j+1] :
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            # IF no two elements were swapped by inner loop, then break
            if swapped == False:
                break

        return nums

    def insertion_sort(self,nums):
        nums_length = len(nums)
        # Traverse through 1 to len(arr)
        for i in range(1, nums_length):
            key = nums[i]
            # Move elements of nums[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and key < nums[j] :
                    nums[j+1] = nums[j]
                    j -= 1
            nums[j+1] = key

nums = [2,3,4,2,1,1,1,2]
sorting = Sorting()
print(sorting.selection_sort(nums))
