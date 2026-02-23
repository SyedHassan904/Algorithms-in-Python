
unsorted_list=[3,1,2,4,7,9,1,3,3,3,2,2]
# unique_value_of_unsorted_list=set(unsorted_list)
max_value=max(unsorted_list)
sorted_list=[0]*(len(unsorted_list))
frequency_list=[0]*max_value
def counting_sort(unsorted_list,sorted_list,max_value):
    # for i in unique_value_of_unsorted_list:
    #     frequency=unsorted_list.count(i)
    #     frequency_list[i-1]=frequency
    for num in unsorted_list:
        frequency_list[num-1]+=1
    
    for i in range(1,len(frequency_list)):
        frequency_list[i]=frequency_list[i-1]+frequency_list[i]
    
    for i in range(len(unsorted_list)-1,-1,-1):
        sorted_list[frequency_list[unsorted_list[i]-1]-1]=unsorted_list[i]
        frequency_list[unsorted_list[i]-1]-=1
        
counting_sort(unsorted_list,sorted_list,max_value)
print(sorted_list)