import random

unsorted_list=[20,13,1,16,2,17,3,18,4]
start_index=0
end_index=len(unsorted_list)-1


def partition(arr,start_index,end_index):
    pivot_value=arr[start_index]
    q=start_index
    for j in range(start_index+1,end_index+1):
        if pivot_value>arr[j]:
            q+=1
            arr[q],arr[j]=arr[j],arr[q]
    arr[q],arr[start_index]=arr[start_index],arr[q]
    return q

def quick_sort(arr,start_index,end_index):
    if start_index<end_index:
        random_index=random.randint(start_index,end_index)
        arr[random_index],arr[start_index]=arr[start_index],arr[random_index]
        pivot_index=partition(arr,start_index,end_index)
        quick_sort(arr,start_index,pivot_index-1)
        quick_sort(arr,pivot_index+1,end_index)

quick_sort(unsorted_list,start_index,end_index)
print(unsorted_list)