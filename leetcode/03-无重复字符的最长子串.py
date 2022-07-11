"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        start = -1     # 左边初始值
        max = 0      # 最大长度
        d = {}       # 将字符串的字母存到字典中，key为字母，value为位置

        for i in range(len(s)):  # 根据字符串长度，循环字符串的 index
            if s[i] in d and d[s[i]] > start:  # 判断 i 位置的值是否在字典d的key中，判断i位置的值当key在字典中的value值是否大于左边初始值start；
                start = d[s[i]]  # 上面判断成立，证明遇到字母重复，将start移动到重复字母第一个的位置上
                d[s[i]] = i     # 将重复字母的第二个数字赋值给字典上对应key的值；
            else:
                d[s[i]] = i    # 不成立，添加或者修改key对应的值；
                if i - start > max:  # 如果i-start为不重复字母的长度，大于max，则更新max值；
                    max = i - start
        return max


if __name__ == '__main__':
    l = "abcbbdfhjeefaghzxa"
    s = Solution()
    i = s.lengthOfLongestSubstring(l)
    print(i)
