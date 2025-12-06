from pprint import pprint as pp


input_str = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

with open("part01_input.txt") as f:
    input_str = f.read()

print(input_str)

def parse_input(input_str):
    lines = input_str.strip().split('\n')
    operators = lines[-1].split()
    number_lines = lines[:-1]
    cols = min([len(l) for l in number_lines])
    number_groups = []
    group = []
    pp([len(l) for l in number_lines])
    print(f"Cols: {cols}")
    for c in range(cols):
        if all(l[c] == ' ' for l in number_lines):
            number_groups.append(group)
            group = []
            continue
        digits = ""
        for l in number_lines:
            digits = digits + l[c]
        print(f"Digits at col {c}: '{digits}'")
        number = int(digits.strip())
        group.append(number)
    if len(group) > 0:
        number_groups.append(group)
    return number_groups, operators

number_cols, operators = parse_input(input_str)
pp(number_cols)
pp(operators)

grand_total = 0
for col, op in zip(number_cols, operators):
    if op == '*':
        result = 1
        for num in col:
            result *= num
    elif op == '+':
        result = sum(col)
    print(result)
    grand_total += result
print("Grand Total:", grand_total)