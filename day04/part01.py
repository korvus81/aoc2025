from pprint import pprint as pp 

input_str = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

with open("part01_input.txt") as f:
    input_str = f.read().strip()

input = [list(line) for line in input_str.splitlines()]
pp(input)

def count_adjacent_rolls(input, r, c):
    deltas = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]
    count = 0
    for rd,cd in deltas:
        rr = r + rd
        cc = c + cd
        if 0 <= rr < len(input) and 0 <= cc < len(input[0]):
            if input[rr][cc] == '@':
                count += 1
    return count

movable = []
for r,row in enumerate(input):
    for c in range(len(row)):
        if input[r][c] == '@':
            adjacent_rolls = count_adjacent_rolls(input, r, c)
            print(f"Cell ({r},{c}) has {adjacent_rolls} adjacent rolls")
            if adjacent_rolls < 4:
                movable.append((r,c))

for r in range(len(input)):
    for c in range(len(input[0])):
        if input[r][c] == '@':
            if (r,c) in movable:
                print("x", end="")
                continue 
        print(input[r][c], end="")
    print()
print(f"Total movable rolls: {len(movable)}")