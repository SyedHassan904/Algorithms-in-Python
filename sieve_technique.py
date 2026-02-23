
data = [10,20,30,40,50,60]
# data=[5, 9, 2, 6, 4, 1, 3, 7]

def choose_pivot(li,start_index):
    return li[start_index]


def partition(li,start_index,end_index,pivot_point):
    x=pivot_point
    temp_list = [0]*(end_index-start_index+1)
    temp_i=0
    # Place elements smaller than pivot
    for i in range(start_index, end_index + 1):
        if li[i]<x:
            temp_list[temp_i]=li[i]
            temp_i+=1
    
    pivot_index=start_index+temp_i
    temp_list[temp_i]=x
    temp_i+=1
    
    # Place elements greater than pivot
    for i in range(start_index,end_index+1):
        if li[i]>x:
            temp_list[temp_i]=li[i]
            temp_i+=1
    
    # Copy only subarray back
    j=0
    for i in range(start_index,end_index+1):
        li[i]=temp_list[j]
        j+=1
    
    return pivot_index


# Optimized Method for partition
# def partition(li,start_index,end_index,pivot_point):
#     pivot=pivot_point
#     q=start_index
#     s=start_index+1
#     for i in range(s,end_index):
#         if li[s]<pivot:
#             q=q+1
#             li[q],li[s]=li[s],li[q]
#     li[start_index],li[q]=li[q],li[start_index]
#     return q
        
    

def select(li,start_index,end_index,k):
    if start_index==end_index:
        return li[start_index]
    else:
        x=choose_pivot(li,start_index)
        q=partition(li,start_index,end_index,x)
        rank_x=q-start_index+1
        if k==rank_x:
            return x
        if k<rank_x:
            return select(li,start_index,q-1,k)
        else:
           return select(li,q+1,end_index,k-rank_x)

print(select(data,0,len(data)-1,5))



    