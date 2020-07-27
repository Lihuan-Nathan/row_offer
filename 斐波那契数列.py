# -*- coding:utf-8 -*-
import time
class Solution:
    def Fibonacci(self, n):
        # write code here
        # F(0) = 0,   F(1) = 1
        # F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
       
        
        indexs = []  # 保存下标的数组
        values = []  # 保存下标对应的值的数组
        if (n==0):
            return 0
        elif (n==1):
            return 1
        elif (n>1):
            if (n-1) not in indexs:
                indexs.append(n-1)
                values.append(self.Fibonacci(n-1))
            if (n-2) not in indexs:
                indexs.append(n-2)
                values.append(self.Fibonacci(n-2))
            if (n-1) in indexs and (n-2) in indexs:
                return values[indexs.index(n-1)]+values[indexs.index(n-2)]
        return None



    def Fibonacci1(self, n):
        # write code here
        # F(0) = 0,   F(1) = 1
        # F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
        
        
        # indexs = []  # 保存下标的数组
        # values = []  # 保存下标对应的值的数组
        if (n==0):
            return 0
        elif (n==1):
            return 1
        elif (n>1):
            # if (n-1) not in indexs:
            #     indexs.append(n-1)
            #     values.append(self.Fibonacci(n-1))
            # if (n-2) not in indexs:
            #     indexs.append(n-2)
            #     values.append(self.Fibonacci(n-2))
            # if (n-1) in indexs and (n-2) in indexs:
            #     return values[indexs.index(n-1)]+values[indexs.index(n-2)]
            return self.Fibonacci1(n-1)+self.Fibonacci1(n-2)
        return None

    

    def xunhuan(self,n):
        
        a = 1  # 较大
        b = 0  # 较小
        for i in range(0,n-1):
            sum = a + b
            b = a
            a = sum

        return sum


if __name__ == "__main__":
    
    s = Solution()
    start_time = time.time()
    print(s.Fibonacci(30))   # 使用辅助数组
    end_time = time.time()
    print(end_time-start_time)

    print("=============================================")

    start_time1 = time.time()
    print(s.Fibonacci1(30))  # 直接递归
    end_time1 = time.time()
    print(end_time1-start_time1)


    print("=============================================")

    start_time2 = time.time()
    print(s.xunhuan(30))   #循环方法
    end_time2 = time.time()
    print(end_time2-start_time2)


