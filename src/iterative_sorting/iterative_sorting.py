# TO-DO: Complete the selection_sort() function below 
# 5, 3, 4, 2, 8
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j   
        # TO-DO: swap
        x = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = x
    print(arr)
    return arr

selection_sort([5, 3, 2, 5, 6])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr