# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
        tour=[]
        find_tour(graph[0][0],graph,tour)
        return tour
        

def find_tour(u,E,tour): 
    for (a,b) in E:
        if a==u:
            E.remove((a,b))
            find_tour(b,E,tour)
        elif b==u:
            E.remove((a,b))
            find_tour(a,E,tour)
    tour.insert(0,u)

find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
