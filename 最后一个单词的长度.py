# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

# 如果不存在最后一个单词，请返回 0 。

# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

# 输入: "Hello World"
# 输出: 5

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        # trail = len(s) - 1
        # head = len(s) -1
        # # import pdb; pdb.set_trace()
        # while(s[head]!=' '):
        #     head = head-1
        
        # # head在‘ ’ trail在末尾 找到子串  
        # substr = s[head+1:trail+1]      #为什么要加1 是因为后面的是不包含这个数的
        # # import pdb; pdb.set_trace()
        # if (substr.isalpha()):
        #     return len(substr)
        

        li = s.split(" ")
        end = len(li)-1
        if li[end].isalpha():
            return len(li[end])
        else:
            return  0
s = "a"
l = Solution().lengthOfLastWord(s)
print(l)

            