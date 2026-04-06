def MoveZeroes(arr):
    j = 0  # position for next non-zero

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        print(arr,i,j)

arr=[2,1,3,4,2,4,0 ,0 ,2,2,0,2,1,2,4,2,6,7]
MoveZeroes(arr)