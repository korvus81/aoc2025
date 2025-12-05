from pprint import pprint as pp 


input_str = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

with open("part01_input.txt") as f:
    input_str = f.read()

def parse_input(input_str):
    sections = input_str.strip().split("\n\n")
    fresh_ranges = []
    for line in sections[0].splitlines():
        start, end = map(int, line.split("-"))
        fresh_ranges.append((start, end))
    ingredients = [int(line) for line in sections[1].splitlines()]
    return fresh_ranges, ingredients

fresh_ranges, ingredients = parse_input(input_str)

# sort so they are in order
fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])
print("Starting ranges:")
pp(fresh_ranges)
print()
changed = True
while changed:
    changed = False
    merged_ranges = []
    current_start, current_end = fresh_ranges[0]
    for start, end in fresh_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
            changed = True
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = start, end
    merged_ranges.append((current_start, current_end))
    fresh_ranges = merged_ranges
print("Merged ranges:")
pp(fresh_ranges)
print()
fresh_count = 0
for range in fresh_ranges:
    #print(f"Fresh range: {range[0]} to {range[1]}")
    fresh_count += (range[1] - range[0]) + 1
print(f"\nTotal fresh ingredients: {fresh_count}")