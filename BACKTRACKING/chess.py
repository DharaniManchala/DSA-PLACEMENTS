def knightTour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    # possible moves
    moves_x = [2, 2, -2, -2, 1, 1, -1, -1]
    moves_y = [1, -1, 1, -1, 2, -2, 2, -2]
    
    # start position
    board[0][0] = 0
    
    def isSafe(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1
    
    def solve(x, y, move_count):
        if move_count == n * n:
            return True
        
        for i in range(8):
            next_x = x + moves_x[i]
            next_y = y + moves_y[i]
            
            if isSafe(next_x, next_y):
                board[next_x][next_y] = move_count
                
                if solve(next_x, next_y, move_count + 1):
                    return True
                
                # backtrack
                board[next_x][next_y] = -1
        
        return False
    
    if solve(0, 0, 1):
        return board
    else:
        return "No solution"


# Example
result = knightTour(5)
for row in result:
    print(row)def knightTour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    # possible moves
    moves_x = [2, 2, -2, -2, 1, 1, -1, -1]
    moves_y = [1, -1, 1, -1, 2, -2, 2, -2]
    
    # start position
    board[0][0] = 0
    
    def isSafe(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1
    
    def solve(x, y, move_count):
        if move_count == n * n:
            return True
        
        for i in range(8):
            next_x = x + moves_x[i]
            next_y = y + moves_y[i]
            
            if isSafe(next_x, next_y):
                board[next_x][next_y] = move_count
                
                if solve(next_x, next_y, move_count + 1):
                    return True
                
                # backtrack
                board[next_x][next_y] = -1
        
        return False
    
    if solve(0, 0, 1):
        return board
    else:
        return "No solution"


# Example
result = knightTour(5)
for row in result:
    print(row)
    