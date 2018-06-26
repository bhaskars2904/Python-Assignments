import numpy
arr = numpy.loadtxt("IntegerArray.txt")

def mergeSort(arr, tmp, l, r):
    """
    Input: arr, ndarray with input numbers. tmp, an empty array of size that of arr. l, left index of arr. r, right index of arr
    Output: Returns the number of inversions in arr
    """
    leftCount = 0 #number of inversions in only left half
    rightCount = 0 #number of invesions in only right half
    splitCount = 0 #number of inverions from left to right or right to left halves
    if r>l:
        m=(l+r)//2
        leftCount = mergeSort(arr, tmp, l, m)
        rightCount = mergeSort(arr, tmp, m+1, r)
        splitCount = merge(arr, tmp, l, m+1, r)
    return leftCount+rightCount+splitCount
    
def merge(arr, tmp, l, m, r):
    """
    Input: arr, ndarray with input numbers. tmp, an empty array of size that of arr. l, left index of arr. m, middle index of arr. 
           r, right index of arr
    Output: Returns the number of split inversions
    """
    count = 0
    a = l
    b = m
    c = l
    while a<=m-1 and b<=r:
        if arr[a] <= arr[b]: #no split inversion
            tmp[c] = arr[a]
            c += 1
            a += 1
        else:
            tmp[c] = arr[b] #split inversion otherwise
            c += 1
            b += 1
            count += m-a    
    while a<=m-1:           #filling out the remaining elements if any
        tmp[c] = arr[a]
        c += 1
        a += 1
    while b<=r:
        tmp[c] = arr[b]
        c += 1
        b += 1
    for i in range(l,r+1,1):
        arr[i] = tmp[i]
    return count

tmp = [0]*len(arr)
print "Numeber of Inversions = "+str(mergeSort(arr, tmp, 0, len(arr)-1))
           
    
