
coin_dominations=[1,5,6,9]
# coin dominations are in rows
# amount is in columns
rows=len(coin_dominations)+1
amount=10
matrix=[[0]*(amount+1) for _ in range(rows)]

def coin_change_problem(amount,coins):
    
    for i in range(1,len(coins)+1):
        for j in range(amount+1):
            # We are only allowed to use the first coin, and the target amount j is smaller than that coin.
            if(i==1 and j<coins[i-1]):
                matrix[i][j] = 0
            
            elif(i==1):
                matrix[i][j]=1+matrix[1][j-coins[i-1]]
            
            elif(j<coins[i-1]):
                matrix[i][j]=matrix[i-1][j]
            
            else:
                matrix[i][j]=min(matrix[i-1][j],1+matrix[i][j-coins[i-1]])
                

            
coin_change_problem(amount,coin_dominations)

print("Minimum coins to make", amount, ":", matrix[len(coin_dominations)][amount])
