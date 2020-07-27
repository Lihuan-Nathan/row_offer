class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        
        
        # 给一个辅助栈
        stack = []
        
        for item in pushV:
            if stack == []:
                stack.append(item)
                continue
            if stack[-1]!=popV[0]:
                stack.append(item)
            if stack[-1]==popV[0]:
               # import pdb; pdb.set_trace()
                stack.pop()
                del popV[0]
        
        while(stack != []):
            if (stack[-1]==popV[0]):
                stack.pop()
                del popV[0]
            else:
                return False

        if stack==[]:
            return True
        
        

if __name__ == "__main__":
    s = Solution()
    pushV = [1,2,3,4,5]
    popV = [4,5,3,2,1]
    ret = s.IsPopOrder(pushV,popV)
    print(ret)