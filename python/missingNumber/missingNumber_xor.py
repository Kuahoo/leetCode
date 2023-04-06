#!/usr/bin/env python3

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for index in range(len(nums)+1):
            result ^= index
        for index in nums:
            result ^= index
        return result


def main():
    nums = [3, 0, 1]
    nums2 = [0, 1]
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    T = Solution()
    print("{} {}".format("Result: ", T.missingNumber(nums)))
    print("{} {}".format("Result: ", T.missingNumber(nums2)))
    print("{} {}".format("Result: ", T.missingNumber(nums3)))


if __name__ == '__main__':
    main()
