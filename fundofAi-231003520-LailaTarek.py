import time
#---------------------------------------------------------------------------
def check_validation(board, row, column, N):  # Check column
    for i in range(row):   
        if board[i][column] == 1:  # Check each row before the current row
            return False
        
    # Check major diagonal (top-left to bottom-right)
    for i in range(row):   
        if column - row == board[i].index(1) - i if 1 in board[i] else False:  
            return False
    
    # Check minor diagonal (top-right to bottom-left)
    for i in range(row): 
        if column + row == board[i].index(1) + i if 1 in board[i] else False:
            return False

    return True

#---------------------------------------------------------------------------
from collections import deque

def BFS(N):
    queue = deque([([[0] * N for _ in range(N)], 0)])  # Initialize board and first row
    s_count = 0  # Solution count
    created_nodes = 1  # Start with the root node

    start_bfs_time = time.time()

    visited_node = []

    while queue:
        board, row = queue.popleft()

        if len(visited_node) < 5:
            visited_node.append(board)

        if row == N:
            s_count += 1
            continue

        for column in range(N):
            if check_validation(board, row, column, N):
                new_board = [r[:] for r in board]
                new_board[row][column] = 1
                queue.append((new_board, row + 1))
                created_nodes += 1  # Increment the node count for every new node created

    end_bfs_time = time.time()
    laila = end_bfs_time - start_bfs_time

    return s_count, laila, created_nodes, visited_node

#---------------------------------------------------------------------------
def DFS(N):
    stack = [([[0] * N for _ in range(N)], 0)]  # Initialize board and first row
    solution_count = 0  # Solution count
    created_nodes = 1  # Start with the root node

    start_dfs_time = time.time()

    visited_nodes = []

    while stack:  # Process stack nodes
        board, row = stack.pop()

        if len(visited_nodes) < 5:
            visited_nodes.append(board)

        if row == N:  # All queens are placed
            solution_count += 1
            continue

        for column in range(N):
            if check_validation(board, row, column, N):
                new_board = [r[:] for r in board]
                new_board[row][column] = 1
                stack.append((new_board, row + 1))
                created_nodes += 1  # Increment the node count for every new node created

    end_dfs_time = time.time()

    bash_samar = end_dfs_time - start_dfs_time

    return solution_count, bash_samar, created_nodes, visited_nodes

#---------------------------------------------------------------------------
N = int(input("Enter the size of the board (N): "))

bfs, time_b, nodes_b, bfs_visited = BFS(N)
print(f"BFS solutions for a {N}x{N} board: {bfs}, took {time_b:.2f} sec, nodes created: {nodes_b}")

dfs, time_d, nodes_d, dfs_visited = DFS(N)
print(f"\nDFS solutions for a {N}x{N} board: {dfs}, took {time_d:.2f} sec, nodes created: {nodes_d}")

if time_b < time_d:
    print(f"Lola tele3et asra3 (; (BFS ya3ni)")
elif time_b == time_d:
    print("mota3adlin |;")
else:
    print(f"keda keda bash samar asra3 akeed (DFS)")

if nodes_b < nodes_d:
    print(f"BFS is more efficient in terms of created nodes ({nodes_b} < {nodes_d})")
elif nodes_b == nodes_d:
    print("Both BFS and DFS created the same number of nodes.")
else:
    print(f"DFS is more efficient in terms of created nodes ({nodes_d} < {nodes_b})")
