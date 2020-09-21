adj={1:[2,4],
     2:[3],
     3:[1],
     4:[5],
     5:[]
    }

def dfs(adj,u,visited,stack):
    for v in adj[u]:
        if visited[v]==False:
            visited[v]=True
            dfs(adj,v,visited,stack)
    stack.append(u)
    return(stack)

def transpose(adj):
    new_adj={}
    for i in adj:
        for j in adj[i]: 
            if j in new_adj:
                new_adj[j].append(i)
            else:
                new_adj[j]=[i]
    return(new_adj)

def dfs_2(adj,u,visited,comp):
    for v in adj[u]:
        if visited[v]==False:
            visited[v]=True
            dfs_2(adj,v,visited,comp)
        comp.append(u)
    return(comp)

cnt=0
visited={}
stack=[]

for i in adj:
    visited[i]=False

for i in adj:
    if visited[i]==False:
        visited[i]=True
        stk=(dfs(adj,i,visited,stack))
nw_ad=transpose(adj)

for i in nw_ad:
    visited[i]=False

for i in range(len(stk)-1,-1,-1):
    if visited[stk[i]]==False:
        comp=[]
        cnt+=1
        visited[stk[i]]=True
        dfs_2(nw_ad,stk[i],visited,comp)
        print("Component",cnt,"->",comp)
print("No. of Strongly Connected Components are -", cnt)    

