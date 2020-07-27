
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    
    head = 0
    trail = len(nums) - 1
    
    while head<trail:
        if nums[head]!=val:
            head = head+1
        else:
            if nums[trail] == val:
                trail = trail - 1
            
            # 交换
            nums[head] = nums[trail]
            nums[trail] = val

    # 退出说明找完了

    # 删除
    
    t = len(nums)-(trail+1)
    i = 0
    while i<= t:
        nums.pop()
        i = i+1
    
    return len(nums)

nums = [2,3,2,3]
val = 3
ret = removeElement(nums,val)
print(ret)

    