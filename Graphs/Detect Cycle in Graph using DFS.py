adj_list={
    "A" : ["C", "B"],
    "B" : ["D"],
    "C" : [],
    "D" : ["A", "E"],
    "E" : []
}

status={}
parent={}
dfs_algo=[]
cycle=False

for node in adj_list:
    status[node]='u'
    parent[node]=None

def check_cycle(u):
    global cycle
    status[u]='a'
    dfs_algo.append(u)
    for v in adj_list[u]:
        if status[v]=='u':
            parent[v]=u
            check_cycle(v)
        elif status[v]=='a':
            if parent[u]!=v:
                cycle=True
                print("Cycle Found at", u,v)
                break
    status[u]='v'

check_cycle('A')
print(dfs_algo)
if cycle==False:
    print("No Cycle Found")
