aw_input = input("Enter Data in Array: ")
arr = [int(x) for x in raw_input.split()]

# Display stored data
print("Stored Data in Array:", " ".join(map(str, arr)))

# Get 0-based index/position to delete
pos = int(input("Enter poss. of Element to Delete: "))

# Delete element at specific position
if 0 <= pos < len(arr):
    arr.pop(pos)
    print("New data in Array:", " ".join(map(str, arr)))
else:
 print("Invalid position!")
