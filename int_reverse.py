def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        stack  = []
        str_ret = ""
        flag = ''
        for x in str_x:
            if x=='-':
                flag = '-'
                continue
            stack.append(x)
        # return stack

        if flag =='-':
            str_ret = '-'
        while(stack):
            str_ret = str_ret + stack.pop() 

        return int(str_ret)

print(reverse(-123))
print(reverse(123))