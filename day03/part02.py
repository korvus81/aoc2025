

input_str = """987654321111111
811111111111119
234234234234278
818181911112111"""

with open("part01_input.txt", "r") as f:
    input_str = f.read().strip()

banks = input_str.splitlines()

total_joltage = 0
for banknum,bank in enumerate(banks):
    vals = [int(x) for x in bank]
    digits = []
    digit_indexes = []
    last_index = -1
    for i in range(12, 0, -1):
        current_max = max(vals[last_index+1:len(vals)-i+1]) 
        digits.append(current_max)
        digit_index = vals.index(current_max,last_index+1)
        digit_indexes.append(digit_index)
        last_index = digit_index
    bank_joltage = 0
    for d in digits:
        bank_joltage = bank_joltage * 10 + d
    total_joltage += bank_joltage 
    print(f"Bank {banknum+1} - Digits: {digits} (ind: {digit_indexes}), Bank joltage: {bank_joltage}, Total joltage so far: {total_joltage}")
