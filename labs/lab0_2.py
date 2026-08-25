def count_mines(board, i, j, n):
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0),  (1,1)]
    return sum(
        1 for di, dj in directions
        if 0 <= i+di < n and 0 <= j+dj < n and board[i+di][j+dj] == "#"
    )

if __name__ == "__main__":
    n = int(input().strip())
    board = [input().split() for _ in range(n)]

    result = [
        [
            board[i][j] if board[i][j] == "#" else str(count_mines(board, i, j, n))
            for j in range(n)
        ]
        for i in range(n)
    ]

    for row in result:
        print("   ".join(row))
