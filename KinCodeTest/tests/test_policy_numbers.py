import numpy as np
import pytest

# Assuming the code you provided is in a module named `module`
from KinCodeTest.getpolicynumbers import read_file_to_drawings, extract_digit_blocks, match_digit_pattern, extract_numbers_from_drawings, validate_checksum, process_files_in_directory

# Sample data for testing
SAMPLE_DRAWING_1 = """\
 _  
|_|
  |
"""
SAMPLE_DRAWING_2 = """\
 _   _ 
|_| |_|
 _|  _|
"""
SAMPLE_DRAWING_3 = """\
 _   _   _  
|_  |_  |_ 
 _|  _|  _|
"""

# Sample patterns
SAMPLE_PATTERNS = {
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

def test_read_file_to_drawings():
    with open('test_file.txt', 'w') as f:
        f.write(SAMPLE_DRAWING_1 + '\n\n' + SAMPLE_DRAWING_2)
    
    drawings = read_file_to_drawings('test_file.txt')
    assert len(drawings) == 2
    assert drawings[0].strip() == SAMPLE_DRAWING_1.strip()
    assert drawings[1].strip() == SAMPLE_DRAWING_2.strip()

def test_extract_digit_blocks():
    digit_blocks = extract_digit_blocks(SAMPLE_DRAWING_1)
    print(digit_blocks[0])
    assert len(digit_blocks[0]) == 3
    assert digit_blocks[0] == [' _ ', '|_|', '  |']


def test_match_digit_pattern():
    for digit, pattern in SAMPLE_PATTERNS.items():
        assert match_digit_pattern(pattern) == digit

def test_extract_numbers_from_drawings():
    drawings = [SAMPLE_DRAWING_1, SAMPLE_DRAWING_2]
    numbers_list = extract_numbers_from_drawings(drawings)
    assert numbers_list[0] == '?'

def test_validate_checksum():
    valid_number = '831488126'
    invalid_number = '1234567?9'
    
    assert validate_checksum(valid_number) == True
    assert validate_checksum(invalid_number) == False

