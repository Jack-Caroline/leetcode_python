"""
给你一个字符串 s，找到 s 中最长的回文子串。

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

输入：s = "cbbd"
输出："bb"
"""


class Solution:
    def longestPalindrome(self, s):
        palindrome = ''

        for i in range(len(s)):
            len1 = len(self.getlongestpalindrome(s, i, i))

            if len1 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i)

            len2 = len(self.getlongestpalindrome(s, i, i + 1))

            if len2 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i + 1)

        return palindrome

    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
