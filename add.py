import pdb
def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    
    ids = []
    for item in nums:
        j_id = 0
        for it in nums:
            pdb.set_trace() 
            if j_id<=i:
                j_id= j_id+1
                continue
            if it+item == target:
                ids.append(i)
                ids.append(j_id)
                return ids
            j_id = j_id+1
        i = i+1

nums = [3,2,4]
target = 6
print(twoSum(nums,target))