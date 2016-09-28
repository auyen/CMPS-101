import os
from multiprocessing import Queue
from collections import deque

class Graph(object):
    # Initializing empty graph
    def __init__(self):
        self.adj_list = dict()    # Initial adjacency list is empty dictionary
        self.vertices = set()    # Vertices are stored in a set
        self.degrees = dict()    # Degrees stored as dictionary

    # Checks if (node1, node2) is edge of graph. Output is 1 (yes) or 0 (no).
    def isEdge(self,node1,node2):
        if node1 in self.vertices:        # Check if node1 is vertex
            if node2 in self.adj_list[node1]:    # Then check if node2 is neighbor of node1
                return 1            # Edge is present!

        if node2 in self.vertices:        # Check if node2 is vertex
            if node1 in self.adj_list[node2]:    # Then check if node1 is neighbor of node2
                return 1            # Edge is present!

        return 0                # Edge not present!

    # Add undirected, simple edge (node1, node2)
    def addEdge(self,node1,node2):

        # print('Called')
        if node1 == node2:            # Self loop, so do nothing
            # print('self loop')
            return
        if node1 in self.vertices:        # Check if node1 is vertex
            nbrs = self.adj_list[node1]        # nbrs is neighbor list of node1
            if node2 not in nbrs:         # Check if node2 already neighbor of node1
                nbrs.add(node2)            # Add node2 to this list
                self.degrees[node1] = self.degrees[node1]+1    # Increment degree of node1

        else:                    # So node1 is not vertex
            self.vertices.add(node1)        # Add node1 to vertices
            self.adj_list[node1] = {node2}    # Initialize node1's list to have node2
            self.degrees[node1] = 1         # Set degree of node1 to be 1

        if node2 in self.vertices:        # Check if node2 is vertex
            nbrs = self.adj_list[node2]        # nbrs is neighbor list of node2
            if node1 not in nbrs:         # Check if node1 already neighbor of node2
                nbrs.add(node1)            # Add node1 to this list
                self.degrees[node2] = self.degrees[node2]+1    # Increment degree of node2

        else:                    # So node2 is not vertex
            self.vertices.add(node2)        # Add node2 to vertices
            self.adj_list[node2] = {node1}    # Initialize node2's list to have node1
            self.degrees[node2] = 1         # Set degree of node2 to be 1

    # Give the size of the graph. Outputs [vertices edges wedges]
    #
    def size(self):
        n = len(self.vertices)            # Number of vertices

        m = 0                    # Initialize edges/wedges = 0
        wedge = 0
        for node in self.vertices:        # Loop over nodes
            deg = self.degrees[node]      # Get degree of node
            m = m + deg             # Add degree to current edge count
            wedge = wedge+deg*(deg-1)/2        # Add wedges centered at node to wedge count
        return [n, m, wedge]            # Return size info

    # Print the graph
    def output(self,fname,dirname):
        os.chdir(dirname)
        f_output = open(fname,'w')

        for node1 in list(self.adj_list.keys()):
            f_output.write(str(node1)+': ')
            for node2 in (self.adj_list)[node1]:
                f_output.write(str(node2)+' ')
            f_output.write('\n')
        f_output.write('------------------\n')
        f_output.close()

    def path(self, src, dest):
        queue = deque() # Creates queue that is iterated through
        visited = set() # Creates set for visited vertices
        dist = dict() # Creates dictionary for distance from source for each thespian
        pred = dict() # Creates dictionary for predecessor of each thespian
        for vert in self.vertices: # For vertices set distance to 0 and predecessor to None
            dist[vert] = 0
            pred[vert] = None

        visited.add(src) # Add source to visited
        dist[src] = 0 # Set distance of source to 0
        pred[src] = None # Set predecessor of source to None
        queue.append(src) # Add source to the queue
        while (len(queue) != 0): # While the queue is not empty 
            u = queue[0] # u = head of the queue
            for x in self.adj_list[u]: # For each neighbor of u
                if x not in visited: # If neighbor has not been visited already
                    visited.add(x) # Add neighbor to visited
                    pred[x] = u # Predecessor of neighbor = u
                    dist[x] = dist[u] + 1 # Increment the distance for that neighbor
                    queue.append(x) # Add the neighbor to the queue
            queue.popleft() # Remove the head of the queue

        shortest_path = [] # Stores thespians in shortest path -- this is returned

        for i in range(dist[dest]+1): # For the distance of the destination
            shortest_path.append(dest) # Add the destination to shortest_path
            a = pred[dest] # a = predecessor of the destination
            dest = a # destination = a

        shortest_path.reverse() # Reverse the list

        return shortest_path

    def levels(self, src):
        level_sizes = [] # Stores the size of each level -- this is returned
        level_sizes.append(1) # For level 0, there is 1 thespian with distance 0 
        for i in range (0,6): # For the rest of the levels, set number of thespians to 0
            level_sizes.append(0)
        queue = deque() # Creates queue that is iterated through
        visited = set() # Creates set for visited vertices
        dist = dict() # Creates dictionary for distance from source for each thespian
        for vert in self.vertices: # For vertices set distance to 0
            dist[vert] = 0

        visited.add(src) # Add source to visited set
        dist[src] = 0 # Set distance for source to 0
        queue.append(src) # Add source to the queue
        while (len(queue) != 0): # While the queue is not empty
            u = queue[0] # u = head of the queue
            for x in self.adj_list[u]: # For each neighbor of u
                if x not in visited: # If neighbor has not been visited already
                    count = 1
                    visited.add(x) # Add to visited
                    dist[x] = dist[u] + 1 # Increment the distance for that neighbor
                    queue.append(x) # Add the neighbor to the queue
                    if dist[x] < 6: # If the distance is less than 6 increment count of nodes for that distance
                        level_sizes[dist[x]] += count
                    else: # Else increment count for distance greater than 6
                        level_sizes[6] += count
            queue.popleft() # Remove the head of the queue

        return level_sizes
