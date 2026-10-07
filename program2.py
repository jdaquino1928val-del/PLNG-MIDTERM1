numbers = []
for i in range(8):
    num = int(input(f"Enter integer {i + 1}: "))
numbers.append(num)

# Task 1: Remove duplicate elements
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f"Array after removing duplicates: {unique_numbers}")

# Task 2 & 3: Find second largest and second smallest elements
if len(unique_numbers) < 2:
    print("Cannot find second largest or second smallest (all entered numbers were identical).")
else:
# Sort unique numbers to easily determine positions
    unique_numbers.sort()

second_smallest = unique_numbers[1]
second_largest = unique_numbers[-2]

print(f"Second smallest element: {second_smallest}")
print(f"Second largest element: {second_largest}")
