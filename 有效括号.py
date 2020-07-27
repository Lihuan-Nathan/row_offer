# 20. 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true
# 示例 2:

# 输入: "()[]{}"
# 输出: true
# 示例 3:

# 输入: "(]"
# 输出: false
# 示例 4:

# 输入: "([)]"
# 输出: false
# 示例 5:

# 输入: "{[]}"
# 输出: true



# 20. 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true
# 示例 2:

# 输入: "()[]{}"
# 输出: true
# 示例 3:

# 输入: "(]"
# 输出: false
# 示例 4:

# 输入: "([)]"
# 输出: false
# 示例 5:

# 输入: "{[]}"
# 输出: true



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        stack = []
        flag = False
        
        # 

        left_flag = ['(','{','[']
        right_flag = [')','}',']']
        # head = 0


        if s == "":
            return True
        if len(s)%2!=0:
            return False
        
        else:
            for item in s:
                # 遇到左括号压栈
                if item in left_flag:
                    # stack.clear()
                    stack.append(item)

                end_index  = len(stack) - 1
                # 遇到右括号
                if item in right_flag :
                    if stack:
                        # 查看是不是与栈顶元素匹配
                        top_item = stack[end_index]
                        if item == ')' and top_item == '(':
                            stack.pop()
                        elif item == '}' and top_item == '{':
                            stack.pop()
                        elif item == ']' and top_item == '[':
                            stack.pop()   
                        else:
                            return False     


            if stack:
                return False
            else:
                return True 
           
        



    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        stack = []
        flag = False
        
        # 

        left_flag = ['(','{','[']
        right_flag = [')','}',']']
        # head = 0


        if len(s) == '':
            return True
        if len(s)%2!=0:
            return False
        
        else:
            for item in s:
                # 遇到左括号压栈
                if item in left_flag:
                    # stack.clear()
                    stack.append(item)
                    flag = True
                end_index  = len(stack) - 1
                # 遇到右括号

                import pdb; pdb.set_trace()
                if item in right_flag :
                    if stack:
                        # 查看是不是与栈顶元素匹配
                        top_item = stack[end_index]
                        if item == ')' and top_item == '(':
                            stack.pop()
                        elif item == '}' and top_item == '{':
                            stack.pop()
                        elif item == ']' and top_item == '[':
                            stack.pop()   
                        else:
                            return False     


            if flag:
                if stack:
                    return False
                else:
                    return True 
            else:
                return False
        


s = "[])"
ret = Solution().isValid(s)       
print(ret)