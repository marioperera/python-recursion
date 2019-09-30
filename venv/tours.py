def create_tour(tours):
    # todo
    return []

def get_degree(tour):
    degree ={}
    for x,y in tour:
        degree[x] =degree.get(x,0) +1
        degree[y] =degree.get(y,0) +1

    return degree

def check_edge(t,b,nodes):
    if t[0] ==b:
        if t[1] not in nodes:
            return t[1]
        elif t[1] ==b:

