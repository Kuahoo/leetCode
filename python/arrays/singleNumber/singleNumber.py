#!/usr/bin/env python3
# Given a non-empty array of integers nums, every element appears
# twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity
# and use only constant extra space.

# nums [2, 2, 1, 1] - output 1
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        resultNumber = 0
        for num in nums:
            resultNumber ^= num
        return resultNumber


def main():
    nums = [2, 2, 1]
    nums2 = [4, 1, 2, 1, 2]
    nums3 = [1]
    T = Solution()
    print("{} {}".format("Result: ", T.singleNumber(nums)))
    print("{} {}".format("Result: ", T.singleNumber(nums2)))
    print("{} {}".format("Result: ", T.singleNumber(nums3)))


if __name__ == '__main__':
    main()
