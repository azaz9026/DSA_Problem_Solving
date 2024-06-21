## Recurrence Relation -> T(n) = T(m-p) + T(q-m) + n
## Best Case Scenario -> T(n) = T(n/2) + T(n/2) + n => O(n logn)
## Worst Case Scenario -> T(n) = T(n-1) + n => O(n^2)
## function definition of partition algorithm -> O(n)
def partition(arr, p, q):
    i = p
    ## starting element as a pivot element
    pivot = arr[p]
    for j in range(i+1, q+1):
        if arr[j] <= pivot:
            i += 1
            ## swap between the arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    ## swap between the arr[i] and the pivot element
    arr[i], arr[p] = arr[p], arr[i]
    return i

## function definition of quickSort
def quickSort(arr, p, q):
    if p < q:
        ## function calling for partition algorithm
        mid = partition(arr, p, q)
        ## recursive call for left subtree
        ## T(mid-p)
        quickSort(arr, p, mid-1)
        ## recursive call for right subtree
        ## T(q-mid)
        quickSort(arr, mid+1, q)
    return arr

## Driver code
arr = [20, 10, 5, 70, 50, 89, 34]
p = 0
q = len(arr) - 1
## function calling
result = quickSort(arr, p, q)
print("Sorted array after applying the quickSort is:", result)