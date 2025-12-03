

input_str = """987654321111111
811111111111119
234234234234278
818181911112111"""

with open("part01_input.txt", "r") as f:
    input_str = f.read().strip()

banks = input_str.splitlines()

total_joltage = 0
for i,bank in enumerate(banks):
    vals = [int(x) for x in bank]
    # ind1 = len(vals)-2
    # ind2 = len(vals)-1
    # start_val = vals[ind1]*10 + vals[ind2]
    first_digit = max(vals[:-1]) # largest value in the first half
    first_digit_index = vals.index(first_digit)
    second_digit = max(vals[first_digit_index+1:]) # largest value in the second half
    bank_joltage = first_digit * 10 + second_digit
    total_joltage += bank_joltage 
    print(f"Bank {i+1} - First digit: {first_digit}, Second digit: {second_digit}, Bank joltage: {bank_joltage}, Total joltage so far: {total_joltage}")
