
#NAME: Md. ASIF HASSAN
#ID: 19201029

def a_star_search(start, goal):
        open_fringe = set(start)
        close_fringe = set()
        g = {} #store distance from starting node
        parents = {}# parents contains an adjacency map of all nodes

        #ditance of starting node from itself is zero
        g[start] = 0

        #start is root node i.e it has no parent nodes
        #so start is set to its own parent node
        parents[start] = start   #start node

        while len(open_fringe) > 0:
            n = None
            #node with lowest f() is found
            for v in open_fringe:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v

            if n == goal or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    #nodes 'm' not in first and last set are added to first
                    #n is set its parent
                    if m not in open_fringe and m not in close_fringe:
                        open_fringe.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight


                    #for each node m,compare its distance from start i.e g(m) to the
                    #from start through n node
                    else:
                        if g[m] > g[n] + weight:
                            #update g(m)
                            g[m] = g[n] + weight
                            #change parent of m to n
                            parents[m] = n

                            #if m in closed set,remove and add to open
                            if m in close_fringe:
                                close_fringe.remove(m)
                                open_fringe.add(m)

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the goal
            # then  begin reconstructing the path from it to the start
            if n == goal:
                path = []
                path_cp = []
                full = {
                'H': "Mugda",
                'K': "Komolapur",
                'MOT': "Motijheel",
                'G': "Gulisthan",
                'P': "Polton",
                'SHA': "Shabag",
                'BM': "Bangla Motor",
                'F': "Farmgate",
                'SJ': "Shahjahanpur",
                'MOU': "Mouchak",
                'B': "Basabo",
                'MRG': "Malibagh Rail Gate",
                'U': "UAP"
                }
                while parents[n] != n:
                    path.append(n)
                    path_cp.append(full[n])
                    n = parents[n]

                path.append(start)
                path_cp.append(full[start])
                path.reverse()
                path_cp.reverse()
                print('Path found: {}'.format(str(path_cp).replace(",","-->")))
                return path

            open_fringe.remove(n)
            close_fringe.add(n)

        print('Path does not exist!')
        return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):

        H_dist = {

            'H': 6,
            'K': 5,
            'MOT': 3,
            'G': 4,
            'P': 2,
            'SHA': 1,
            'BM': 1,
            'F': 3,
            'SJ': 4,
            'MOU': 4,
            'B': 5,
            'MRG': 4,
            'U': 0
        }
        return H_dist[n]

Graph_nodes = {

        'H': [('K',2.0), ('B',1.4)],
        'K': [('MOT', 1.3), ('SJ',1)],
        'MOT': [('G', 1.3), ('P', 1.3)],
        'G': [('P', .70)],
        'P': [('SHA', 2)],
        'SHA': [('BM', 1)],
        'BM': [('F', 2.5)],
        'F': [('U',0.25)],
        'SJ': [('MOU', 1)],
	    'MOU': [('BM', 2.8)],
	    'B': [('MRG', 2.3)],
        'MRG': [('BM', 3.3)],
        'U': None
}

path = a_star_search('H','U') 

path_cost = 0.0

for i in range(len(path)-1):
    for key, value in Graph_nodes[path[i]]:
        if key == path[i+1]:
            path_cost += value
            break
print("The path cost is %.2f Km" % path_cost)