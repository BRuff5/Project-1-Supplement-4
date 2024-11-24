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
    

