'''
Dikshta's Shortest Path Algorithm calculates the shortest distance of a node from a source node. It works on the principle of Greedy Algorithm being greedy at each step for the shortest path.

'''


adj={1:[[2,6],[3,4]],
     2:[[1,6],[3,1],[5,6]],
     3:[[1,4],[2,1],[4,2]],
     4:[[3,2],[5,3],[6,11]],
     5:[[2,6],[4,3],[6,1]],
     6:[[4,11],[5,1]]
    }

def shortest_path(adj, dist, priority_q):
    while len(priority_q)!=0:
        x,y=min(priority_q)
        for v in adj[y]:
            if v[1]+x<dist[v[0]]:
                if (dist[v[0]],v[0]) in priority_q:
                    priority_q.pop(priority_q.index((dist[v[0]],v[0])))
                dist[v[0]]=v[1]+x
                priority_q.append((dist[v[0]],v[0]))
        priority_q.pop(priority_q.index(min(priority_q)))
    print(dist[1:])


dist=[999999]*7
priority_q=[]		# To keep record of the shortest distance of the nodes 					from the source node.
dist[1]=0

priority_q.append((dist[1],1))
shortest_path(adj,dist,priority_q)

