# Sum of list elements

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

print("Total:", total)

# Find maximum number

max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum:", max_num)