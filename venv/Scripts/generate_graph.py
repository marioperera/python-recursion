import math as Math


def make_link(G,node1,node2):
    if node1 not in G:
        G[node1] ={}
    (G[node1])[node2] =1
    if node2 not in G:
        G[node2] ={}
    (G[node2])[node1] =1
    return G

G ={}

max_size =256
sides =int(Math.sqrt(max_size))

for i in range(max_size):
    for j in range(max_size):
        if i<max_size-1: make_link(G ,(i,j),(i+1,j))
        if j<max_size-1: make_link(G,(i,j),(i,j+1))

print(len(G))

# how many edges
print (sum(len(G[node]) for node in G.keys())/2)

print(G)