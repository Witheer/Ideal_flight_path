from collections import defaultdict
from collections import deque

# See instructions.md
def ideal_flight_path(flights, home, vacation):
  # 1. Build the graph!
  # 2. BFS!
  # 3. Retrace your steps!
  graph = build_graph(flights)
  path = bfs(graph, home, vacation)
  return retrace_steps(vacation, path)
  
# 1. Build the graph!
# Return an adjacency list representation
def build_graph(flights):
  graph = defaultdict(list)

  for src, dst in flights:
    graph[src].append(dst)

  return graph

# 2. BFS!
# Return the `parent` map of backpointers
def bfs(graph, src, dst):
  Queue = deque()
  # src is the first Node
  parent = {}
  parent[src] = None
  Queue.append(src)

  while Queue:
    node = Queue.popleft()
    
    if node == dst:
      return parent
    
    for children in graph.get(node):
      if children not in parent:
        parent[children] = node
        Queue.append(children)

  # return whatever we had so far
  return parent
      
# 3. Retrace your steps!
# Return the path from src to dst
def retrace_steps(dst, parent):
  if dst not in parent:
    return None
    
  path = deque()
  path.append(dst)
  node = parent.get(dst)
  
  while node:
    path.appendleft(node)
    node = parent.get(node)

  return " -> ".join(path)

# 4. You should probably write some more test cases

flights = [('Detroit', 'Seattle'), ('Seattle', 'Vancouver'), ('Vancouver', 'Las Vegas')]

print(ideal_flight_path(flights, 'Detroit', 'Las Vegas'))

