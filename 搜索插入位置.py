
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # 二分查找
    head = 0
    trail = len(nums) -1

    while(head<=trail):

        mid = int((head+trail)/2)

        if target>nums[mid]:
            head = mid+1
        
        if target<nums[mid]:
            trail = mid-1

        if target == nums[mid]:
            return mid

    return head


nums = [1,3,5,6]
target = 2

print(searchInsert(nums,target))