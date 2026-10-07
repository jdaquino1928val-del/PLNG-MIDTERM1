

# Read 10 real numbers into an array (list)
numbers = []
for i in range(10):
 num = float(input(f"Enter real number {i + 1}: "))
numbers.append(num)

# Task 1: Find sum and average of positive numbers (using a separate loop)
positive_sum = 0.0
positive_count = 0

for num in numbers:
    if num > 0:
        positive_sum += num
positive_count += 1

if positive_count > 0:
    positive_avg = positive_sum / positive_count
    print(f"Sum of positive numbers: {positive_sum}")
    print(f"Average of positive numbers: {positive_avg}")
else:
    print("No positive numbers were entered.")

# Task 2: Count negative numbers (using a separate loop)
negative_count = 0
for num in numbers:
    if num < 0:
        negative_count += 1

print(f"Count of negative numbers: {negative_count}")

# Task 3: Find the minimum value (using a separate loop)
min_val = numbers[0]
for num in numbers[1:]:
    if num < min_val:
        min_val = num

print(f"Minimum value in the array: {min_val}")