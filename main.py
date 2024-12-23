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
    return ', ' .join(string_list)

    """
    Convert a list of strings to a comma-delimited string.
    Args:
        string_list (list): A list of strings.
    Returns:
        str: A comma-delimited string.
    """

def write_to_csv(headers, data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  
        writer.writerow(data)     
        
    """
    Compiles headers and data to a CSV file.
    Args:
        Headers: Creates headers for the CSV file.
        Data: Stores the data in CSV file.
    Result:
        Creates the CSV file
    """
    
def read_and_display_csv(filename):
    print("\nThe CSV file includes:")
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))
            
    """
    Read the contents of a CSV file and print it.
    Args:
        Filename: The name of the CSV file to read.
    Result: 
        The contents of the CSV file.
    """
    
if __name__ == "__main__":
    user_input = input("Enter a number: ")
    
    """
    Creates user input.
    Args:
        user_input: creates and stores user_input.
    Result: 
        input("Enter a number: ".
    """
    
    try:
        num = int(user_input)  
        
        """
        Converts input to an integer.
        Args:
            Takes input and turns into integer
        """
    
        next_numbers = get_next_ten_numbers(num)
    
        """
        Gets the next ten numbers
        Args:
        Get the next 10 numbers.
        """
    
        next_numbers_string = list_to_comma_delimited_string(next_numbers)
    
        """
        Convert the next numbers to a comma-delimited string
        Args:
        Convert the next numbers to a comma-delimited string
        """
    
    
        headers = ["Starting Number", "Next 10 Numbers"]
        data = [str(num), next_numbers_string]
    
        """
        Create headers and data for CSV file
        Args:
            Create headers and data for CSV file
        Result:
            Data and Headers stored in CSV file
        """
    
        filename = 'output.csv'
        write_to_csv(headers, data, filename)
    
        """
        Create the CSV file for the program
        Args:
            Creates a CSV file
        Result:
            CSV file is created and connected to program
        """
    
        print(f"Next 10 numbers: {next_numbers_string}")
        print(f"Data written to '{filename}'")
        read_and_display_csv(filename)
        """Display results
        Args:
            pulls next_numbers_string and CSV (filename)
        Results:
            prints the data in the CSV file
        """

    except ValueError:
        print("Please enter a valid number.")
        """
        Args:
            pulls the the user input 
        Results:
            If the input was valid or not
        """
         