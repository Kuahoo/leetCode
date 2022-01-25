#!/usr/bin/python3
class Solution(object):
    def containsDuplicate(self, nums):
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
