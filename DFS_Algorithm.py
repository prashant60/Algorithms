adj_list={
    "A":["B", "C"],
    "B":["A", "E"],
    "C":["A", "F"],
    "D":["E", "F"],
    "E":["B", "D"],
    "F":["C", "D"]
}

'''
adj_list={
    "A":["B", "C"],
    "B":["D", "E"],
    "C":["B", "F"],
    "D":[],
    "E":["F"],
    "F":[]
}

adj_list={
    "A":["B"],
    "B":["A", "D", "E"],
    "C":["F"],
    "D":["B"],
    "E":["B"],
    "F":["C"]
}
'''

status={}
parent={}
time={}
dfs_traversal=[]

for node in adj_list:
    status[node]='u'
    parent[node]=None
    time=-1

def dfs(u):
    status[u]='a'
    dfs_traversal.append(u)
    for v in adj_list[u]:
        if status[v]=='u':
            parent[v]=u
            dfs(v)
    status[u]='v'

for node in adj_list:
    if status[node]=='u':
        dfs(node)
print(dfs_traversal)
