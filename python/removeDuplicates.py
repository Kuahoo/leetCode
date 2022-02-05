#Leetcode Problem 26: remove duplicates from sorted array.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Python solution that takes O(1) memory.
        """
        unique = 0
        for index in range(len(nums)-1):
            if nums[index] != nums[index+1]:
                nums[unique+1] = nums[index+1]
                unique = unique+1
        return unique+1
        """
        Simple Python solution that is more readable
       
        uniqueNums = sorted(set(nums))
        return len(uniqueNums)
        """
