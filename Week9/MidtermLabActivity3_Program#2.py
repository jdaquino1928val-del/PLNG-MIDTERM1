
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(f"First name: {first_name}")
print(f"Last name: {last_name}")


full_name = first_name + " " + last_name
print(f"Full name: {full_name}")


print(f"First character: {full_name[0]}")
print(f"Last character: {full_name[-1]}")


try:
    first_name[0] = "D"
except TypeError:
    print("Strings are immutable; individual characters cannot be changed directly.")


new_name = "D" + first_name[1:]
print(f"New name: {new_name}")
print(f"Original name: {first_name}")


print("Characters in the full name:")
for char in full_name:
    print(char)


sliced_first = full_name[0:len(first_name)]
sliced_last = full_name[len(first_name) + 1:]
print(f"Sliced first name: {sliced_first}")
print(f"Sliced last name: {sliced_last}")


while True:
    search_char = input("Enter one character to search: ")
    if len(search_char) == 1:
        break
    print("Invalid input. Please enter exactly one character.")

index = full_name.find(search_char)
if index != -1:
    print(f"Character '{search_char}' found at index: {index}")
else:
    print(f"Character '{search_char}' not found.")

print(f'The blank line printed above during the loop is the space in "{full_name}".')
