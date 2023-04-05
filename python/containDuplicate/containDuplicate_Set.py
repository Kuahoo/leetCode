#!/usr/bin/env python3

# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = {}
        for num in nums:
            if num in numSet:
                return True
            numSet[num] = num
        return False

def main():
    nums = [1,2,3,4]
    nums2 = [1,2,3,1]
    T = Solution()
    print("{} {}".format("Result: ", T.containsDuplicate(nums)))
    print("{} {}".format("Result: ", T.containsDuplicate(nums2)))
    
if __name__ == '__main__':
    main()
