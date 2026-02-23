
# tuple first value is weight and second value shows profit
items=[(1,1),(2,6),(5,18),(6,22),(7,28)]

#Knapsack maximum capacity
Weight=11 
n=len(items)
rows=n+1
columns=Weight+1
matrix=[[0 for j in range(columns)] for i in range(rows)]
keep_matrix=[[0 for j in range(columns)] for i in range(rows)]
def knapsack(n,W,matrix,values):
  
    for row in range(1,n+1):
        weight_i=values[row-1][0]
        val_i=values[row-1][1]
        for col in range(W+1):
            if(weight_i<=col and val_i+matrix[row-1][col-weight_i]>matrix[row-1][col]):
                matrix[row][col]=val_i+matrix[row-1][col-weight_i]
                keep_matrix[row][col]=1
            else:
                matrix[row][col]=matrix[row-1][col]
                keep_matrix[row][col]=0
  
def main():
    knapsack(n,Weight,matrix,items)
    col=Weight
    for i in range(n,0,-1):
        if(keep_matrix[i][col]==1):
            value_i=items[i-1][1]
            wt_i=items[i-1][0]
            print(value_i)
            col-=wt_i
        
main()
    
        

    