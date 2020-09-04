adj_list={
    "A":["B", "D"],
    "B":["A", "C"],
    "C":["B"],
    "D":["A", "E", "F"],
    "E":["D", "F", "G"],
    "F":["D", "E", "H"],
    "G":["E", "H"],
    "H":["G", "F"]
}

visited={}
level={}
parent={}
bfs_traversal=[]
queue=[]

for node in adj_list.keys():
    visited[node]=False

start='A'
visited[start]=True
parent[start]=None
level[start]=0
queue.append(start)

while len(queue)is not 0:
    u=queue.pop(0)
    bfs_traversal.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.append(v)
print(bfs_traversal)

print("Shortest Distance between Node G from source is : ", end="")
print(level['G'])

print("Shortest Path")

v="G"
path=[]
while v is not None:
    path.append(v)
    v=parent[v]
path.reverse()
print(path)
