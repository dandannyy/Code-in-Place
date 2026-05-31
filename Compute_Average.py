# Week 6
"""
It is often the case that we don't want to hardcode and store 
large amounts of data directly in the code of our programs. 
Instead, it is more common for us to transport data using files and 
read the data from the files to then operate on it. This also lets 
us operate on different files which are structured the same using 
the same exact code! The starter code already loads a list of numbers 
from file. You may find it interesting to read over. 

Your job is to compute the average of the values in 
number_list and to print the result out.
"""

def main():
    number_list = load_numbers_from_file("numbers.txt")
    total_nums = 0
    for number in number_list:
        total_nums = total_nums + number
    average = total_nums / len(number_list)
    print("Average:", average)
    
def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    return numbers

if __name__ == '__main__':
    main()
