
grid = [
    "#..#..",
    ".#....",
    "#.....",
    ".#....",
    "...#.."
]

class Robot:
    directions = ["up", "right", "down", "left"]

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, grid):
        if grid[self.x][self.y] == ".":
            grid[self.x][self.y] = "C"

        dx, dy = 0, 0
        if self.direction == "up":
            dx, dy = -1, 0
        elif self.direction == "right":
            dx, dy = 0, 1
        elif self.direction == "down":
            dx, dy = 1, 0
        elif self.direction == "left":
            dx, dy = 0, -1

        while True:
            nx, ny = self.x + dx, self.y + dy
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                break
            if grid[nx][ny] == "#":
                break
            self.x, self.y = nx, ny
            if grid[self.x][self.y] == ".":
                grid[self.x][self.y] = "C"

    def turn(self):
        idx = Robot.directions.index(self.direction)
        self.direction = Robot.directions[(idx + 1) % 4]


class Game:
    def __init__(self, grid, start_x1, start_y1, start_x2, start_y2, dir1, dir2):
        self.grid = [list(row) for row in grid]
        self.robot1 = Robot(start_x1, start_y1, dir1)
        self.robot2 = Robot(start_x2, start_y2, dir2)

    def simulate(self, steps=15):
        for _ in range(steps):
            self.robot1.move(self.grid)
            self.robot2.move(self.grid)
            self.robot1.turn()
            self.robot2.turn()

    def cleaned_count(self):
        return sum(row.count("C") for row in self.grid)


x1, y1, dir1 = input().split()
x2, y2, dir2 = input().split()

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

game = Game(grid, x1, y1, x2, y2, dir1, dir2)
game.simulate(15)
print(game.cleaned_count())
