'''
Connected Components in an Undirected Graph.

A component of a graph is connected if the vertices of the graph
is connected to each other by a path which may or may not be immediate.


'''

#'''
adj={
    1:[2,4],
    2:[1,3],
    3:[2,4],
    4:[1,3],
    5:[6,7],
    6:[5,8],
    7:[5],
    8:[6],
    9:[10,11],
    10:[9],
    11:[9],
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

    status[u]='v'
    return trav

status={}
parent={}
trav=[]
cnt=0
for i in adj:
    parent[i]=None
    status[i]='u'

for i in adj:
    if status[i]=='u':
        cnt+=1
        tr=dfs(adj,i,parent, status)
    
print(tr)
print(cnt)
