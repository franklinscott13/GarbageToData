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

def read_file_to_lines(filename):
    with open(filename, 'r') as file:
        return file.read().strip().split('\n')

def extract_digit_blocks(lines):
    num_digits = len(lines[0]) // 4  # Each digit block is 3 characters wide + 1 space
    digit_blocks = []

    for i in range(0, len(lines[0]), 4):
        block = [line[i:i+3] for line in lines]
        digit_blocks.append(block)

    return digit_blocks

def match_digit_pattern(array_2d):
    for digit, pattern in DIGIT_PATTERNS.items():
        if np.array_equal(array_2d, pattern):
            return digit
    return '?'  # Return '?' if no match is found

def extract_numbers_from_lines(lines):
    digit_blocks = extract_digit_blocks(lines)
    numbers = []

    for block in digit_blocks:
        digit_array = np.array(block)
        number = match_digit_pattern(digit_array)
        numbers.append(number)

    return ''.join(numbers)

# Example usage
filename = 'KinCodeTestData.txt'
try:
    lines = read_file_to_lines(filename)
    numbers = extract_numbers_from_lines(lines)
    print(f'Extracted numbers: {numbers}')
except ValueError as e:
    print(f'Error: {e}')

