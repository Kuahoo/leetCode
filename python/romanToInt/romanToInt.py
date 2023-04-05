#!/usr/bin/python3
class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        retInt = 0
        romanString = list(s)
        while len(romanString) > 1:
            currChar = romanString.pop(0)
            nextChar = romanString[0]
            currVal = romanDict[currChar]
            nextVal = romanDict[nextChar]
            if currVal < nextVal:
                retInt -= currVal
            else:
                retInt += currVal
        if len(romanString) == 1:
            currChar = romanString.pop(0)
            currVal = romanDict[currChar]
            retInt += currVal

        return retInt


def main():
    mainStr = 'MCDLXXVI'
    myInt = Solution.romanToInt(mainStr)
    print(myInt)


if __name__ == "__main__":
    main()
