# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

# 示例:

# 输入: 38
# 输出: 2 
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。



# 循环算法

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
      
        add = 0
        if num < 10:
            return num
        str_num = str(num)
        for it in str_num:
            add = add + int(it)
        return self.addDigits(add)


s = Solution().addDigits(38)
print(s)