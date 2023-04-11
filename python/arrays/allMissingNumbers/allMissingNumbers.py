#!/usr/bin/env python3

# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not
# appear in nums.

# approach #1 - sort array, then check index against values in array.
# if index is equal to value then skip, else move to next index,
# use while loop?
# n = 8
# [4, 3, 2, 6, 8, 2, 3, 1] - original
# [1, 2, 2, 3, 3, 4, 7, 8] - sorted order
# [1, 2, 3, 4, 7, 8]       - set order

class Solution(object):
    def allMissingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenOfNums = len(nums)
        numSet = set(nums)
        returnArray = []
        for idx in range(1, lenOfNums+1):
            if idx in numSet:
                pass
            else:
                returnArray.append(idx)
        return returnArray


def main():
    nums = [4, 3, 2, 7, 8, 2, 4, 1]
    nums2 = [1, 1]
    # nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    T = Solution()
    print("{} {}".format("Result: ", T.allMissingNumber(nums)))
    print("{} {}".format("Result: ", T.allMissingNumber(nums2)))
    # print("{} {}".format("Result: ", T.missingNumber(nums3)))


if __name__ == '__main__':
    main()
