 # 1 2 3 4
# 3 4 5 6
# 7 8 9 10




def Find(target, array):
    col = len(array[0])
    # 先确定在那一行
    #import pdb; pdb.set_trace()
    for arr in array:
        if target>arr[col-1]:
            continue
        if target == arr[col-1]:
            return True
        if target<(arr[col-1]):
            # 在二分查找在不在

            min = 0
            max = col-1
            

            while(min<=max):
                mid = int((min+max)/2)
                if target>arr[mid]:
                    min = mid+1
                if target<arr[mid]:
                    max = mid-1
                if target == arr[mid]:
                    return True
            
            if min>max:
                continue
    
    return False

if __name__ == '__main__':
    array = [
            [1, 2, 3 ,4],
            [3, 4 ,5 ,6],
            [7, 8 ,9 ,10]
        ]

    array = [
                [1,4,7,11,15],
                [2,5,8,12,19],
                [3,6,9,16,22],
                [10,13,14,17,24],
                [18,21,23,26,30]
            ]
    array = [[-5]]

    print(Find(-5,array))
    