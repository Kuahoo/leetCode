#!/usr/bin/python3
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type s: str
        :rtype: int
        """
        if len(strs) == 0:
            return ''
            minWordLength = float('inf')
            totalWords = len(strs)
            firstWord = strs[0]
            finalStr = ''

        for word in strs:
            if len(word) < minWordLength:
                minWordLength = len(word)

        if len(strs) == 1:
            return strs[0]
        else:
            while minWordLength > 0:
                stringToCheck = firstWord[:minWordLength]
                stringsMatched = 1
                for word in strs[1:]:
                    currString = word[:minWordLength]
                    if stringToCheck == currString:
                        stringsMatched += 1
                        finalStr = currString
                if stringsMatched == totalWords:
                    print(finalStr)
                    return finalStr
                minWordLength -= 1
            return ''


def main():
    # ex: fl
    strs = ["flower", "flow", "flight"]
    s = Solution()
    s.longestCommonPrefix(strs)


if __name__ == "__main__":
    main()
