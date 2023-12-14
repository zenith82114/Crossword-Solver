# Pattern is (initial_X, initial_Y), direction(D or A), length
# THE WORDS INSERTED SHOULD HAVE THEIR STARTING LETTER CAPITALIZED (For clue names)
# "": {"start":(), "direction":"", "length": },
def make_crossword_grid():
    grid = {}
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        n = len(lines)
        for i in range(0, n, 3):
            clue = lines[i]
            x, y, direction, length = lines[i+1].split()
            grid[clue] = {
                "start":(int(x), int(y)),
                "direction":direction.upper(),
                "length":int(length)
            }
    return grid
