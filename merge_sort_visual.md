li = [99,2,67,1]

[2,99] [1,67]
merge_sort(0,3)
├── merge_sort(0,1)
         merge_sort(0,0)xx
         merge_sort(1,1)xx
         merge(0,0,1)  i=0 , mid=0 , j=1
│   
├── merge_sort(2,3)
          merge_sort(2,2)XX
          merge_sort(3,3)XX
          merge(2,2,3) i=2, mid=2 , j=2+1=3, last=3
│   
└── merge(0,1,3) i=0 , mid=1, j=mid+1=2 , last_index=3
