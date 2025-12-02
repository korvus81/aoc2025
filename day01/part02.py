
from pprint import pprint as pp

def rotate2(current, instruction):
    newpos = current 
    zero_passes = 0
    rotate_amount = int(instruction[1:])
    for i in range(rotate_amount):
        if instruction[0] == 'L':
            newpos = (newpos - 1) % 100
        else:
            newpos = (newpos + 1) % 100
        if newpos == 0:
            zero_passes += 1
    return newpos, zero_passes


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
    current_position,zero_passes = rotate2(current_position, instr)
    print(f"After {instr}, new position: {current_position}")
    count += zero_passes
print(f"Final position: {current_position}")
print(f"Number of times position 0 was reached: {count}")