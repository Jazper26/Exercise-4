def equal(num):
    # Check if the list is not empty
    if num:
        # Compare the first and last elements of the list
        return num[0] == num[-1]
    else:
        # If the list is empty, return False
        return False