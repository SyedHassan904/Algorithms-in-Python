li = [99,2,67,1,1001,46,4,10]

def merge(li,start_index,mid,end_index):
    i=k=start_index
    j=mid+1
    temp=[0]*(end_index+1)
    while(i<=mid and j<=end_index):
        if(li[i]<li[j]):
            temp[k]=li[i]
            k+=1
            i+=1
        else:
            temp[k]=li[j]
            k+=1
            j+=1
    while(i<=mid):
        temp[k]=li[i]
        k+=1
        i+=1
    while(j<=end_index):
        temp[k]=li[j]
        k+=1
        j+=1
    for i in range(start_index, end_index + 1):
        li[i] = temp[i]


def merge_sort(li,start_index,end_index):
    if (start_index<end_index):    
        mid=(start_index+end_index)//2   
        merge_sort(li,start_index,mid)  
        merge_sort(li,mid+1,end_index)   
        merge(li,start_index,mid,end_index)

  
print("Unsorted List are: ", li)      
merge_sort(li,0,len(li)-1)
print("sorted List are: ", li) 