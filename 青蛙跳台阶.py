class Solution:
    def jumpFloor(self, number):
        # write code here
        
        # number 0  0
        # number 1  1
        # number 2  2
        # number 3  3
        # number 4  5
        
        
        if number <1:
            return 0
        if number == 1:
            return 1
        if number ==2:
            return 2
        
        a = 1
        b = 2
        ret = 0
        for i in range(3,number+1):
            ret = a + b      # 两个数相加，相加完毕为下一次循环做准备
            a = b            # 将上一级大的数给小的数
            b = ret         # 将和给大的数
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(4))
    
            