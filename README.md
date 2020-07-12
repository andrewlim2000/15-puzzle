# 15-puzzle
A set of search algorithms that find solutions to the 15-puzzle.

### INPUT:
The program will accept instructions from the command line. The program accepts the following inputs in the following format:  
`"[initialstate]" [searchmethod] [options]`
- `[initialstate]` must contain sixteen characters, namely the digits 1-9, letters A-F, and a space, in any order.
- `[searchmethod]` can be: BFS, DFS, DLS, GBFS, AStar.
- `[options]` are only relevant for DLS (depth-limited search), where the option specifies the maximum depth to explore, GBFS and AStar, where option specifies which heuristic to use.
- Examples:
    - `"123456789AB DEFC" BFS`
    - `"123456789AB DEFC" DFS`
    - `"123456789AB DEFC" DLS 2`
    - `"123456789AB DEFC" GBFS h1`
    - `"123456789AB DEFC" AStar h2`

### OUTPUT:
The output should be a comma-separated list of integers listing the following format. These format should represent the state of the search tree at the moment the solution was discovered.
- `[depth], [numCreated], [numExpanded], [maxFringe]`
- `[depth]` represents the depth in the search tree where the solution is found. The integer will be zero if the solution is at the root and it will be "-1" if a solution was not found.
- `[numCreated]` is the counter that is incremented every time a node of the search tree is created (output 0 if depth == -1).
- `[numExpanded]` is the counter that will be incremented every time the search algorithm acquires the successor states to the current state; i.e. every time a node is pulled off the fringe and found not to be the solution (output 0 if depth == -1).
- `[maxFringe]` is the maximum size of the fringe at any point during the search (output 0 if depth == -1).
- Example:
    - `python FifteenProblem.py "123456789ABC DFE" BFS`
    - `3, 54, 17, 37`