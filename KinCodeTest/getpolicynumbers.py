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

def read_file_to_drawings(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
    # Split by double newlines to separate drawings
    drawings = content.split('\n\n')
    return drawings

def extract_digit_blocks(drawing):
    lines = drawing.split('\n')
    num_digits = len(lines[0]) // 4  # Each digit block is 3 characters wide + 1 space
    digit_blocks = []

    for i in range(num_digits):
        block = [line[i*4:i*4+3] for line in lines if line.strip()]
        digit_blocks.append(block)

    return digit_blocks

def match_digit_pattern(array_2d):
    for digit, pattern in DIGIT_PATTERNS.items():
        if np.array_equal(array_2d, pattern):
            return digit
    return '?'  # Return '?' if no match is found

def extract_numbers_from_drawings(drawings):
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
        weight = 9 - i  # d9 is first, d1 is last
        total += weight * int(digit)
    
    return (total % 11) == 0

def process_files_in_directory(directory):
    with open('results.txt', 'w+') as file: 
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):  # Process only .txt files
                file_path = os.path.join(directory, filename)
                try:
                    drawings = read_file_to_drawings(file_path)
                    numbers_list = extract_numbers_from_drawings(drawings)
                    for idx, numbers in enumerate(numbers_list, start=1):
                        print(f'PossibleNumbers: {numbers}')
                        if validate_checksum(numbers):
                            print(f'Checksum valid for: {numbers}')
                            file.write(str(numbers))
                        else:
                            print(f'Checksum invalid for: {numbers}')
                            if '?' in str(numbers):
                                file.write(str(numbers) + ' ILL' + '\n')
                            else:
                                file.write(str(numbers) + ' ERR'+ '\n')
                except ValueError as e:
                    print(f'Error processing file {filename}: {e}')

# Example usage
directory = 'TestFiles'  # Replace with your directory path
process_files_in_directory(directory)
