# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Outer while loop - iterates through each row
while row < size:
    # Inner for loop - prints asterisks in each row
    for col in range(size):
        print("*", end="")
    
    # Print newline after each row
    print()
    
    # Increment row counter
    row += 1