#剑指 Offer 11. 旋转数组的最小数字
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        ref_value = numbers[0]
        min = 0
        max = len(numbers)-1

        while(True):
            mid =  int((min+max)/2)
            if numbers[mid]>=ref_value:
                min= mid+1
            if numbers[mid]<ref_value:
                max = mid
                break;
        # 找到了一段
        # [min-max]
        temp_numbers = numbers[min:max+1]
        temp_numbers = sorted(temp_numbers);
        return temp_numbers[0]
       


numbers = [3,4,5,1,2]

ret = Solution().minArray(numbers)

print(ret)