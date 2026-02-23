
unsorted_list=[12,1,13,2,4,7,5,3]
num_of_items=len(unsorted_list)

def build_max_heap(arr,last_index):
    last_non_leaf_item=(last_index-1)//2
    for i in range(last_non_leaf_item,-1,-1):
        heapify(arr,i,last_index)
    

def heapify(arr,curr_idx,last_idx):
    left_child_index=(2*curr_idx)+1
    right_child_index=(2*curr_idx)+2
    max=curr_idx
    if(left_child_index<=last_idx and arr[left_child_index]>arr[max]):
        max=left_child_index
    if(right_child_index<=last_idx and arr[right_child_index]>arr[max]):
        max=right_child_index
    
    if(curr_idx != max):
        arr[curr_idx],arr[max]=arr[max],arr[curr_idx]
        heapify(arr,max,last_idx)
    
    
def heap_sort(arr,n):
    last_idx=n-1
    build_max_heap(arr,last_idx)
    for i in range(last_idx,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,0,i-1)

# After each swap (arr[0], arr[i] = arr[i], arr[0]), 
# the element at index i is now in its correct sorted position — it should no longer 
# be part of the heap.
# So you call heapify() only on the remaining unsorted part of the array, which
# goes from index 0 to i-1.
    
heap_sort(unsorted_list,num_of_items)
print(unsorted_list)