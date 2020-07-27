# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        j = 0
        st = []
        for i in s:
            # 等于空格
            #import pdb; pdb.set_trace()
            if (i== ' '):
                #import pdb; pdb.set_trace()
                st.insert(j,'%')
                st.insert(j+1,'2')
                st.insert(j+2,'0')
                j = j+3
            else:
                st.insert(j,i)
                j = j+1
        s1 = ''.join(st)
        return  s1

    def replaceSpace1(self, s):
        s.replace()

if __name__ == '__main__':
   
   s = Solution()
   st = "hello world"
   print(s.replaceSpace(st))
    