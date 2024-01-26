def equal(num):
    # Check if the list is not empty
    if num:
        # Compare the first and last elements of the list
        return num[0] == num[-1]
    else:
        # If the list is empty, return False
        return False

# Given
num_x = [10, 20, 30, 40, 10]
num_y = [75, 65, 35, 75, 30]

# Test the function if it works
res_x = equal(num_x)
res_y = equal(num_y)
