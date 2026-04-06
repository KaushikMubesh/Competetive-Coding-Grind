def QuickSort(arr,low,high):
    if (low>=high):
        return 
    x=low+1
    y=high
    pivot = arr[low]
    i=low+1
    j=high
    while(i<=j):
        while (i<=j and arr[i] >= pivot   ):
            i+=1
        while( i<=j and arr[j] < pivot ):
            j -=1

        if (i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
    arr[x-1], arr[j] = arr[j], arr[x-1]

    QuickSort(arr,x-1,j-1)
    QuickSort(arr,j+1,y)

arr=[2,1,3,5,7,3,64,32,234,23,343,341,12,3,523,31,3,5,7,2]
QuickSort(arr,0,len(arr)-1)
print(arr)