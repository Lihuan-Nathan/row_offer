

def bubbleSort(array,n):
    
    # n = len(array)
    #import pdb; pdb.set_trace()
    for i in range(0,n):
        for j in range(0,n-i-1):
            if array[j+1]<array[j]:
                # jiaohuan
                temp = array[j]
                array[j] = array[j+1]
                array[j+1]= temp   
    return array

if __name__ == '__main__':
    array = [1,9,8,7,6,5]
    print(bubbleSort(array,len(array)))
    
    


