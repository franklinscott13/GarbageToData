import os
import numpy as np

# Define constants for digit patterns
DIGIT_PATTERNS = {
    '0': np.array([' _ ', '| |', '|_|']),
    '1': np.array(['   ', '  |', '  |']),
    '2': np.array([' _ ', ' _|', '|_ ']),
    '3': np.array([' _ ', ' _|', ' _|']),
    '4': np.array(['   ', '|_|', '  |']),
    '5': np.array([' _ ', '|_ ', ' _|']),
    '6': np.array([' _ ', '|_ ', '|_|']),
    '7': np.array([' _ ', '  |', '  |']),
    '8': np.array([' _ ', '|_|', '|_|']),
    '9': np.array([' _ ', '|_|', ' _|'])
}

def read_test_files(filename):
    with open(filename, 'r') as file:
        content = file.read()
    # Split by double newlines to separate drawings
    drawings = content.split('\n\n')
    
    return drawings

def extract_digit_blocks(drawing):
    lines = drawing.split('\n')
    for line in lines:
            print(line)
    num_digits = len(lines[0]) // 4  # Each digit block is 3 characters wide + 1 space
    digit_blocks = []

    for i in range(num_digits):
        block = [line[i*4:i*4+3] for line in lines if line.strip()]  # slices each line to get the 3 characters representing the digit block.
        digit_blocks.append(block)

    return digit_blocks

def match_digit_pattern(array_2d):
    for digit, pattern in DIGIT_PATTERNS.items():
        if np.array_equal(array_2d, pattern):
            return digit
    return '?'  # Return '?' if no match is found

def extract_numbers_from_files(drawings):
    all_numbers = []
    
    for drawing in drawings:
        digit_blocks = extract_digit_blocks(drawing)
        numbers = []

        for block in digit_blocks:
            digit_array = np.array(block)
            number = match_digit_pattern(digit_array)
            numbers.append(number)

        all_numbers.append(''.join(numbers))
    
    return all_numbers

def validate_checksum(number):
    # Ensure the number has exactly 9 digits
    if len(number) != 9 or not number.isdigit():
        return False
    
    total = 0
    for i, digit in enumerate(number):
        weight = i + 1  # d1 has weight 1, d2 has weight 2, ..., d9 has weight 9
        total += weight * int(digit)
    
    return (total % 11) == 0

def process_files_in_directory(directory):
    with open('results.txt', 'w+') as file: 
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):  # Process only .txt files
                file_path = os.path.join(directory, filename)
                try:
                    drawings = read_test_files(file_path)
                    numbers_list = extract_numbers_from_files(drawings)
                    for idx, numbers in enumerate(numbers_list, start=1):
                        print(f'PossibleNumbers: {numbers}')
                        status = "Valid" if validate_checksum(numbers) else ("ILL" if '?' in numbers else "ERR") # if a valid number and not checksum ERR Else ILL or its valid
                        print(f'Checksum {status} for: {numbers}') 
                        file.write(f'{numbers}{" " + status if status != "Valid" else ""}\n') # write to file if not valid add the suffix
                except ValueError as e:
                    print(f'Error processing file {filename}: {e}')

# Example usage
directory = 'TestFiles'  # Replace with your directory path
process_files_in_directory(directory)
