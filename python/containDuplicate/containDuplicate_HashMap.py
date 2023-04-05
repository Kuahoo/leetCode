#!/usr/bin/env python3
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsHashMap = {}
        for num in nums:
            if num in numsHashMap:
                return True
            else:
                numsHashMap[num] = nums 
        return False


def main():
    nums = [1,2,3,4]
    nums2 = [1,2,3,1]
    T = Solution()
    print("{} {}".format("Result: ", T.containsDuplicate(nums)))
    print("{} {}".format("Result: ", T.containsDuplicate(nums2)))

if __name__ == '__main__':
    main()
