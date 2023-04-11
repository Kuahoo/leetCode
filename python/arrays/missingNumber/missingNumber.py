#!/usr/bin/env python3

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

class Solution(object):
    def missingNumber(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in range(0, len(nums)+1):
            if num in nums:
                pass
            else:
                return num


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
