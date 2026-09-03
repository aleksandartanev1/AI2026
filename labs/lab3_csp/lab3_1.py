from constraint import Problem, BacktrackingSolver

def solve(K, table):
    problem = Problem(BacktrackingSolver())

    variables = []
    for i in range(K):
        for j in range(K):
            var = (i, j)
            variables.append(var)
            problem.addVariable(var, [0, 1])

    regions = set()
    for i in range(K):
        for j in range(K):
            regions.add(table[i][j])

    N = len(regions)

    problem.addConstraint(lambda *vals: sum(vals) == N, variables)

    region_cells = {}
    for i in range(K):
        for j in range(K):
            r = table[i][j]
            region_cells.setdefault(r, []).append((i, j))

    for r in region_cells:
        problem.addConstraint(lambda *vals: sum(vals) <= 2, region_cells[r])

    for i in range(K):
        for j1 in range(K):
            for j2 in range(j1 + 1, K):
                if table[i][j1] != table[i][j2]:
                    problem.addConstraint(
                        lambda x, y: not (x == 1 and y == 1),
                        [(i, j1), (i, j2)]
                    )

    for j in range(K):
        for i1 in range(K):
            for i2 in range(i1 + 1, K):
                if table[i1][j] != table[i2][j]:
                    problem.addConstraint(
                        lambda x, y: not (x == 1 and y == 1),
                        [(i1, j), (i2, j)]
                    )

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for i in range(K):
        for j in range(K):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < K and 0 <= nj < K:
                    if table[i][j] == table[ni][nj]:
                        problem.addConstraint(
                            lambda x, y: not (x == 1 and y == 1),
                            [(i, j), (ni, nj)]
                        )

    return problem.getSolution()


if __name__ == '__main__':
    K = int(input())
    grid = [list(map(int, input().split())) for _ in range(K)]

    solution = solve(K, grid)
    if solution is None:
        print('No Solution!')
    else:
        for i in range(K):
            row = []
            for j in range(K):
                if solution[(i, j)] == 1:
                    row.append("*")
                else:
                    row.append(str(grid[i][j]))
            print(" ".join(row))