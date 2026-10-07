size = int(input("Enter Size of Array : "))

# Read array elements
print(f"Enter any {size} elements in Array:")
arr = [int(x) for x in input().split()]

even_elements = []
odd_elements = []

# Separate even and odd numbers
for num in arr:
    if num % 2 == 0:
     even_elements.append(str(num))
else:
 odd_elements.append(str(num))

# Display results
print("\nEven Elements:", " ".join(even_elements))
print("Odd Elements:", " ".join(odd_elements))