
def remove_chars(input_str, i):
    
    # Check if n is within the bounds of the string length
    if i < len(input_str):
        # Use string slicing to remove characters up to index n
        new_str = input_str[i:]
        return new_str
    
    else:
        # If n is greater than or equal to the string length, return an empty string
        return ""

# Examples:
result1 = remove_chars("pynative", 4)
result2 = remove_chars("pynative", 2)

# Print the results
print(f"For 'pynative' with n=4: {result1}")
print(f"For 'pynative' with n=2: {result2}")
