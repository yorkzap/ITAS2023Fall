# Test Cases for `users_choice.py`

This document outlines various test cases for the `users_choice.py` script from the ITAS 185 Introduction to Programming course. These test cases aim to ensure the script runs as expected under different scenarios.

## Test Case Format

Each test case will follow this format:

- **Test Case ID**: A unique identifier for the test case.
- **Description**: A brief description of what the test case is checking.
- **Preconditions**: Any prerequisites or conditions that need to be met before running the test.
- **Test Steps**: Step-by-step instructions to execute the test.
- **Expected Result**: The expected outcome if the script is functioning correctly.
- **Actual Result**: The actual outcome after running the test (to be filled out during testing).
- **Status**: Pass or Fail (to be determined during testing).

## Test Cases

### Test Case 1: Valid Letter and File Input

- **Test Case ID**: TC1
- **Description**: Test the script with a valid single letter and a valid filename.
- **Preconditions**: `users_choice.py` is available and executable; sample text files are present in the directory.
- **Test Steps**:
  1. Run `python users_choice.py`.
  2. Enter a single valid letter when prompted (e.g., 'e').
  3. Choose a valid file from the listed text files.
- **Expected Result**: The script should correctly display the frequency of the letter in the selected file.
- **Actual Result**: The letter 'e' appears 8 times in the file 'yaks.txt'.

### Test Case 2: Invalid Letter Input

- **Test Case ID**: TC2
- **Description**: Test the script with an invalid input (number or special character) as the letter.
- **Preconditions**: `users_choice.py` is available and executable.
- **Test Steps**:
  1. Run `python users_choice.py`.
  2. Enter a number or special character when prompted for a letter (3).
- **Expected Result**: The script should display an error message and prompt for the letter again.
- **Actual Result**: Please enter a letter and not '3'.

### Test Case 3: Multiple Letters Input

- **Test Case ID**: TC3
- **Description**: Test the script with more than one letter as input.
- **Preconditions**: `users_choice.py` is available and executable.
- **Test Steps**:
  1. Run `python users_choice.py`.
  2. Enter more than one letter (e.g., 'ab') when prompted.
- **Expected Result**: The script should display an error message about the input being more than one character.
- **Actual Result**: Please enter a single letter.

### Test Case 4: Non-existent File Input

- **Test Case ID**: TC4
- **Description**: Test the script with a filename that does not exist.
- **Preconditions**: `users_choice.py` is available and executable.
- **Test Steps**:
  1. Run `python users_choice.py`.
  2. Enter a valid letter (e).
  3. Enter a non-existent filename (rr.txt).
- **Expected Result**: The script should display an error message about the file not being found and prompt for another filename.
- **Actual Result**: File 'rr.txt' not found in ./files/part_b. Please enter a valid file name from the following:

### Test Case 5: Handling User Interruption (Ctrl+C)

- **Test Case ID**: TC5
- **Description**: Test how the script handles an unexpected user interruption.
- **Preconditions**: `users_choice.py` is available and executable.
- **Test Steps**:
  1. Run `python users_choice.py`.
  2. Interrupt the script by pressing Ctrl+C.
- **Expected Result**: The script should exit gracefully, displaying a goodbye or cancellation message.
- **Actual Result**: Program exited by user (Ctrl+C).

