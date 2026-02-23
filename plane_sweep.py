

points = [(5,1),(4,4),(2,5),(13,3),(11,5),(7,7),(15,7),
          (14,10),(9,10),(4,11),(12,12),(7,13)]

class stack:
    def __init__(self):
        self.points_list = []
        self.top_index = -1
        
    def push(self,value):
        self.points_list.append(value)
        self.top_index+=1
    
    def pop(self):
        if self.top_index==-1:
            print("Stack is empty")
            return None
        val=self.points_list.pop()
        self.top_index-=1
        return val
    
    def top(self):
        return self.points_list[self.top_index]
    
    def isEmpty(self):
        return self.top_index==-1
    
    def print_stack(self):
        for i in range(self.top_index+1):
            print(self.points_list[i])
    
    
# If I Use Bubble Sort Then the Overall Time Complexity of Plane Sweep Algorithm is
#  O(n^2) So i Used Build-in Sorted Method of Python

# def sorted_points_on_based_x(points):
#     n=len(points)
#     for i in range(n):
#         for j in range(n-i-1):
#             if(points[j][0]>points[j+1][0]):
#                 temp=points[j]
#                 points[j]=points[j+1]
#                 points[j+1]=temp



def plane_sweep(li):
    #used Build-in Python Method for Sorting so Time-Complexity of Algorithm
    # become O(nlogn)
    li.sort(key=lambda p: p[0])
    s=stack()
    n=len(li)
    for i in range(n):
        while(not s.isEmpty() and s.top()[1]<=li[i][1]):
            s.pop()
        s.push(li[i])
    s.print_stack()


plane_sweep(points)


    
    
    
        
                
        
        