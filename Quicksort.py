length = int(raw_input("Enter length of sequence of numbers: \n"))
arr = map(int, raw_input("Enter the sequence of numbers seperated by space: \n").split())
def quickSort(arr,l,r):
    """
    Input: arr, an array of integers. l, left index of arr. r, right index of arr
    Output: Returns nothing
    """
    if l<r:
        pi = partition(arr,l,r)     
        quickSort(arr,l,pi-1)
        quickSort(arr,pi+1,r)

def partition(arr,l,r):
   """
   Input: arr, an array of integers. l, left index of arr. r, right index of arr
   Output: index of partition
   """
   pivot = arr[r] #pivot selected as extreme right element of arr
   parIndex = l #temporary partition index which will end up as sorted index of pivot
   i=l
   while i<r:
       if arr[i]<=pivot:
           arr[i], arr[parIndex] = arr[parIndex], arr[i]
           parIndex += 1           
       i += 1
   arr[parIndex], arr[r] = arr[r], arr[parIndex]
   return parIndex
   
quickSort(arr, 0, length-1) #Time Complexity for quickSort is O(n*n) in worst case and O(nlogn) in average case
print "\nOutput: ",
for i in range(length):
    print (arr[i]),