def safe_write_to_list(lst, index, value):
    try:
        lst[index] = value
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")

# Example usage
my_list = [1, 2, 3]

# Attempt to write to an out-of-bounds index
safe_write_to_list(my_list, 10, 99)
 
