
from pprint import pprint as pp

def rotate(current, instruction):
    newpos = current 
    if instruction[0] == 'L':
        newpos = (current - int(instruction[1:])) % 100
    else:
        newpos = (current + int(instruction[1:])) % 100
    return newpos


instructions = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".strip().splitlines()

with open("part01_input.txt") as f:
    instructions = f.read().strip().splitlines()

pp(instructions)

count = 0
current_position = 50
for instr in instructions:
    current_position = rotate(current_position, instr)
    print(f"After {instr}, new position: {current_position}")
    if current_position == 0:
        count += 1
print(f"Final position: {current_position}")
print(f"Number of times position 0 was reached: {count}")