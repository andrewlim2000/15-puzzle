python FifteenProblem.py "123456789AB DEFC" BFS
1, 4, 1, 3

python FifteenProblem.py "123456789AB DEFC" DFS
1, 4, 1, 3

python FifteenProblem.py "123456789AB DEFC" GBFS h1
1, 4, 1, 3

python FifteenProblem.py "123456789AB DEFC" GBFS h2
1, 4, 1, 3

python FifteenProblem.py "123456789AB DEFC" AStar h1
1, 4, 1, 3

python FifteenProblem.py "123456789AB DEFC" AStar h2
1, 4, 1, 3

python FifteenProblem.py "123456789AB DEFC" DLS 2
1, 4, 1, 3

------------------------------------------------------------

python FifteenProblem.py "123456789 FBDAEC" BFS
100, 213, 100, 113

python FifteenProblem.py "123456789 FBDAEC" DFS
9025, 17603, 9025, 8578

python FifteenProblem.py "123456789 FBDAEC" GBFS h1
12, 27, 12, 15

python FifteenProblem.py "123456789 FBDAEC" GBFS h2
6, 15, 6, 9

python FifteenProblem.py "123456789 FBDAEC" AStar h1
40, 88, 40, 48

python FifteenProblem.py "123456789 FBDAEC" AStar h2
6, 15, 6, 9

python FifteenProblem.py "123456789 FBDAEC" DLS 2
-1, 0, 0, 0

------------------------------------------------------------

Time complexity

b = branching factor
b* = effective branching factor
d = depth of least-cost solution
m = maximum depth
l = depth limit/cutoff

BFS: O(b^d) -> O(4^d)

DFS: O(b^m) -> O(4^m)

GBFS: O(b*^m) ~ O(1^m)
The effective branching factor depends on the heuristic.

AStar: O(b*^d) ~ O(1^d)
The time complexity of A* depends on the heuristic. 
Good heuristics are those with low effective branching factor (the optimal being b* = 1).

DLS: O(b^l) -> O(4^l)
