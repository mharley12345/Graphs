"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

        
    
    
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices ={}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        if vertex_id in self.vertices:
            print("Warning that vertex_id already exists")
        else:
            self.vertices[vertex_id] = set()
       

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
      # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
   
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
         # TODO
        return self.vertices[vertex_id]
   

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO
        # Create an empty queue
        # Add the starting vertex_id to the queue
        # Create an empty set to store visited nodes
        # While the queue is not empty...
            # Dequeue, the first vertex
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add all neighbors to the back of the queue
        #Create an empty queue
        queue = Queue()
        #get starting point
        queue.enqueue(starting_vertex)
        #create set to track visited 
        visited = set()
        #run algo while items are present in queue
        while queue.size() > 0:
            vertex = queue.dequeue()
            # If not visited
            if vertex not in visited:
                # print the vertex and add it to visited
                print(vertex)
                visited.add(vertex)
                # get the edges/neighbors
                for neighbor in self.get_neighbors(vertex):
                    #add the edge to the queue
                    queue.enqueue(neighbor)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #same a bft except use stack instead of queue
          # TODO
        #create stack
        stack = Stack()
        #get starting point
        stack.push(starting_vertex)
        #create set to keep track of visited
        visited = set()
        #run algo while items are present in stack
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    stack.push(next_vert)
     
            
        

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
       #create queue
        queue = Queue()
        # Create starting point
        queue.enqueue([starting_vertex])
        #create visited set
        visited = set()
        # while items in set run algo
        while queue.size() > 0:
            # Pop 1st item
            path = queue.dequeue()
            vertex = path[-1]
            #if not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                # for each edge add the item
                for next_vert in self.get_neighbors(vertex):
                    #copy path to avoid pass by reference bug
                    #mak a copy of path rather then the reference
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)
                    
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            path= stack.pop()
            vertex = path[-1]
            
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        if visited is None:
                visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Printing graph.vertices")
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("Running bft")
    graph.bft(1)
   # graph.bft(2)
   # graph.bft(3)
   # graph.bft(4)
   # graph.bft(5)
   # graph.bft(6)
   # graph.bft(7)
   

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Running dft")
    graph.dft(1)
    print("Running dft_recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Running bfs")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Running DFS")
    print(graph.dfs(1, 6))
    print("Running dfs_recursive")
    print(graph.dfs_recursive(1, 6))
