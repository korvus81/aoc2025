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

fresh_count = 0
for ing in ingredients:
    is_fresh = any(start <= ing <= end for start, end in fresh_ranges)
    status = "fresh" if is_fresh else "not fresh"
    print(f"Ingredient {ing} is {status}.")
    if is_fresh:
        fresh_count += 1
print(f"\nTotal fresh ingredients: {fresh_count}")