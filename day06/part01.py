from pprint import pprint as pp


input_str = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

with open("part01_input.txt") as f:
    input_str = f.read()

def parse_input(input_str):
    lines = input_str.strip().split('\n')
    operators = lines[-1].split()
    
    number_rows = []
    for line in lines[:-1]:
        parts = line.split()
        row = []
        for part in parts:
            row.append(int(part))
        number_rows.append(row)

    number_cols = list(zip(*number_rows))
    return number_cols, operators

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