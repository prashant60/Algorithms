'''
Topological Sorting is for Directed Acyclic Graph (DAG) only.

It is a linear ordering of vertices such that for every directed edge uv,
vertex u always comes before vertex v in the ordering.

Topological Sorting of graph is not possible if graph is not a DAG.
'''

#'''
adj={
    1:[2,3],
    2:[4],
    3:[5],
    4:[5],
    5:[],
    6:[4,5]
    }
#'''
'''
adj={
    0:[],
    1:[],
    2:[3],
    3:[1],
    4:[0,1],
    5:[0,2]
    }
'''

def dfs(adj, u, parent, status):
    status[u]='a'
    trav.append(u)
    for v in adj[u]:
        if status[v]=='u':
            status[v]='a'
            parent[v]=u
            dfs(adj, v, parent, status)
        elif status[v]=='a':
            print("Cycle Detected")

    stack.append(u)

    status[u]='v'
    return stack[::-1]

status={}
parent={}
trav=[]
stack=[]

for i in adj:
    parent[i]=None
    status[i]='u'

for i in adj:
    if status[i]=='u':
        tr=dfs(adj,i,parent, status)
    
print(tr)
