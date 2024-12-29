# nqueen
This project solves the N-Queens problem using Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms. The goal is to compare their performance based on execution time and the number of nodes created during the search.

First, a function called `check_validation` was created to validate the placement of queens. This function ensures that no two queens threaten each other by checking:
1. If there's another queen in the same column.
2. If there's another queen in the same major diagonal (top-left to bottom-right).
3. If there's another queen in the same minor diagonal (top-right to bottom-left).

To validate the major diagonal, the difference between the column and the row of the queen is compared to the current position. If they match, the placement is invalid. Similarly, for the minor diagonal, the sum of the column and row is used. If all checks pass, the function returns true, indicating the queen can be placed.

Next, a `BFS` function was implemented. It initializes an empty `N x N` chessboard, a counter for the number of solutions found, and a `created_nodes` variable set to 1 (representing the initial root node). The nodes are stored in a queue, and the time is recorded at the start of the process. The algorithm pops nodes from the queue, validates placements, and generates new nodes for valid configurations. If a solution is found (all queens placed), the counter is incremented, and the loop skips further checks for that path. The process ends with a calculation of execution time and a count of nodes created. Up to the first five visited nodes are saved for visualization.

The `DFS` function follows a similar logic but uses a stack instead of a queue. This allows the algorithm to explore paths depth-first. Like BFS, it counts the solutions, tracks the number of nodes created, and calculates execution time. The stack-based approach often terminates early when solutions are found, making it faster in some cases.

To run the program, the user inputs the size of the chessboard (`N`). Both algorithms are executed, and their results are displayed, including the number of solutions, execution times, nodes created, and a comparison of efficiency. 

The comparison shows that DFS is often faster for finding solutions, while BFS tends to create more nodes due to its exhaustive level-wise search.



