from collections import deque


edges=[[0,1],[0,2],[0,3],[2,3],[3,1]]
n=4
graph=[list() for _ in range(n)]


# For Undirected graph
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])



def bfs(Graph,scr,n):
    queue=deque()
    visted=[False]*n
    answered_list=[]
    queue.append(scr)
    visted[scr]=True
    while queue:
        curr=queue.popleft()
        answered_list.append(curr)
        for neighbor in Graph[curr]:
            if visted[neighbor] is not True:
                queue.append(neighbor)
                visted[neighbor]=True
    return answered_list

print(bfs(graph,3,n))
        
        