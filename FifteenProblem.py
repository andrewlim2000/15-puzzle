import sys
import copy
import math
from queue import Queue
from queue import PriorityQueue 

# node representing game board
class Node():
    def __init__(self, state, blank):
        self.state = state
        self.blank = blank
        self.successors = []

    def add_successor(self, node):
        self.successors.append(node)

    def __lt__(self, other):
        return other.state < self.state

depth = 0
numCreated = 1
expanded = set()
maxFringe = 1

def create_branches(node):
    global depth
    global numCreated
    if len(node.successors) == 0:
        depth = depth + 1

    # can blank move right?
    if (node.blank + 1) % 4 != 0:
        new_node = copy.deepcopy(node)
        new_node.state[node.blank] = new_node.state[node.blank + 1]
        new_node.state[node.blank + 1] = " "
        new_node.blank = node.blank + 1
        new_node.successors = []

        if str(new_node.state) not in expanded:
            node.add_successor(new_node)
            numCreated = numCreated + 1
            print(new_node.state)

    # can blank move down?
    if math.ceil((node.blank + 1) / 4) != 4:
        new_node = copy.deepcopy(node)
        new_node.state[node.blank] = new_node.state[node.blank + 4]
        new_node.state[node.blank + 4] = " "
        new_node.blank = node.blank + 4
        new_node.successors = []

        if str(new_node.state) not in expanded:
            node.add_successor(new_node)
            numCreated = numCreated + 1
            print(new_node.state)

    # can blank move left?
    if node.blank % 4 != 0:
        new_node = copy.deepcopy(node)
        new_node.state[node.blank] = new_node.state[node.blank - 1]
        new_node.state[node.blank - 1] = " "
        new_node.blank = node.blank - 1
        new_node.successors = []

        if str(new_node.state) not in expanded:
            node.add_successor(new_node)
            numCreated = numCreated + 1
            print(new_node.state) 

    # can blank move up?
    if math.floor(node.blank / 4) != 0:
        new_node = copy.deepcopy(node)
        new_node.state[node.blank] = new_node.state[node.blank - 4]
        new_node.state[node.blank - 4] = " "
        new_node.blank = node.blank - 4
        new_node.successors = []

        if str(new_node.state) not in expanded:
            node.add_successor(new_node)
            numCreated = numCreated + 1
            print(new_node.state)

# Breadth-first	search
def bfs(source):
    global maxFringe
    queue = Queue()
    queue.put(source)

    while not queue.empty():
        if queue.qsize() > maxFringe:
            maxFringe = queue.qsize()
        node = queue.get()
        if node.state == goalState1 or node.state == goalState2:
            print(str(depth) + ", " + str(numCreated) + ", " + 
                str(len(expanded)) + ", " + str(maxFringe))
            return
        expanded.add(str(node.state))
        create_branches(node)
        for successor in node.successors:
            if str(successor.state) not in expanded:
                queue.put(successor)
    
    # solution not found
    print("-1, 0, 0, 0")

# Depth-first search
def dfs(source):
    global maxFringe
    stack = []
    stack.append(source)

    while stack:
        if len(stack) > maxFringe:
            maxFringe = len(stack)
        node = stack.pop()
        if node.state == goalState1 or node.state == goalState2:
            print(str(depth) + ", " + str(numCreated) + ", " + 
                str(len(expanded)) + ", " + str(maxFringe))
            return
        expanded.add(str(node.state))
        create_branches(node)
        list1 = []
        for successor in node.successors:
            if str(successor.state) not in expanded:
                list1.append(successor)
        list1.reverse()
        stack.extend(list1)

    # solution not found
    print("-1, 0, 0, 0")

# Greedy best-first	search
def gbfs(source, h):
    global maxFringe
    pq = PriorityQueue()
    # heuristic
    if h == "h1":
        pq.put((h1(source), source))
    else:
        pq.put((h2(source), source))

    while not pq.empty():
        if pq.qsize() > maxFringe:
            maxFringe = pq.qsize()
        node = pq.get()[1]
        if node.state == goalState1 or node.state == goalState2:
            print(str(depth) + ", " + str(numCreated) + ", " + 
                str(len(expanded)) + ", " + str(maxFringe))
            return
        expanded.add(str(node.state))
        create_branches(node)
        for successor in node.successors:
            if str(successor.state) not in expanded:
                if h == "h1":
                    pq.put((h1(successor), successor))
                else:
                    pq.put((h2(successor), successor))

    # solution not found
    print("-1, 0, 0, 0")

# A* (AStar)
def astar(source, h):
    global maxFringe
    pq = PriorityQueue()
    # heuristic
    if h == "h1":
        pq.put((h1(source), source))
    else:
        pq.put((h2(source), source))

    while not pq.empty():
        if pq.qsize() > maxFringe:
            maxFringe = pq.qsize()
        node = pq.get()[1]
        if node.state == goalState1 or node.state == goalState2:
            print(str(depth) + ", " + str(numCreated) + ", " + 
                str(len(expanded)) + ", " + str(maxFringe))
            return
        expanded.add(str(node.state))
        create_branches(node)
        for successor in node.successors:
            if str(successor.state) not in expanded:
                if h == "h1":
                    pq.put((h1(successor) + depth, successor))
                else:
                    pq.put((h2(successor) + depth, successor))
    
    # solution not found
    print("-1, 0, 0, 0")

# Depth-limited	search (DLS)
def dls(source, limit):
    global maxFringe
    stack = []
    stack.append(source)

    while stack:
        if len(stack) > maxFringe:
            maxFringe = len(stack)
        node = stack.pop()
        if node.state == goalState1 or node.state == goalState2:
            print(str(depth) + ", " + str(numCreated) + ", " + 
                str(len(expanded)) + ", " + str(maxFringe))
            return
        expanded.add(str(node.state))
        create_branches(node)
        if depth <= limit:
            list1 = []
            for successor in node.successors:
                if str(successor.state) not in expanded:
                    list1.append(successor)
            list1.reverse()
            stack.extend(list1)

    # solution not found
    print("-1, 0, 0, 0")

# the number of misplaced tiles
def h1(node):
    num_misplaced = 0
    for x in range(len(goalState1)):
        if node.state[x] != goalState1[x] or node.state[x] != goalState2[x]:
            if node.state[x] != " ":
                num_misplaced += 1
    return num_misplaced

# the sum of the distances of the tiles from their goal positions (Manhattan distance)
def h2(node):
    sum = 0
    for x in range(len(node.state)):
        sum += abs(x // 4 - goalState1.index(node.state[x]) // 4) + \
            abs(x % 4 - goalState1.index(node.state[x]) % 4)
    return sum
            
# instructions
args = sys.argv[1:]

initialState = []
goalState1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', ' ']
goalState2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'F', 'E', ' ']

for x in args[0]:
    initialState.append(x)

initialBlank = initialState.index(' ')

sourceNode = Node(initialState, initialBlank)

def main():
    if args[1] == "BFS":
        bfs(sourceNode)
    elif args[1] == "DFS":
        dfs(sourceNode)
    elif args[1] == "GBFS":
        if args[2] == "h1":
            gbfs(sourceNode, "h1")
        else:
            gbfs(sourceNode, "h2")
    elif args[1] == "AStar":
        if args[2] == "h1":
            astar(sourceNode, "h1")
        else:
            astar(sourceNode, "h2")
    else:
        dls(sourceNode, int(args[2]))

if __name__ ==  "__main__":
    main()