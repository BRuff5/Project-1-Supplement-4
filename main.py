import csv

def get_next_ten_numbers(start_num):
    next_numbers = [str(start_num + i) for i in range(1, 11)]
    return next_numbers

    """
    Return the next 10 numbers after the given number the user inputs.
    Args:
        start_number (int): The starting number.
    Returns:
        list: A list of strings representing the next 10 numbers in the sequeqnce .
    """
    
def list_to_comma_delimited_string(string_list):
    return ', '.join(string_list)
    
    """
    Convert a list of strings to a comma-delimited string.
    Args:
        string_list (list): A list of strings.
    Returns:
        str: A comma-delimited string.
    """