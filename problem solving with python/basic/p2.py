
print("Number Pattern Display")

num = 1  # Initialize num
for i in range(1, 6):  # Outer loop for rows
    num += 1  # Increment num
    for j in range(1, num):  # Inner loop for columns
        print(j, end=" ")  # Print numbers in the row
    print()  # Move to the next line

print("End of Program  1")
