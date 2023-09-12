# 185 Notes

## What is programming?

- **Definition:** Programming is the art, science, and engineering of designing and writing computer programs.

## What is a program?

- **Definition:** A program is a set of instructions that directs the computer's behavior.

## What is Python?

- **Definition:**
    - High-level, general-purpose programming language.
    - Easy to read, dynamically typed, and garbage-collected.
    - Supports multiple paradigms.
    - Comprehensive standard library ("batteries included").

## Different Kinds of Languages

- **Programming Language (High-Level Language):** 
  - Use human-readable code.
  - Requires a compiler or interpreter for execution.
  
- **Machine Language:**
  - Consists of binary and coded commands.
  - Understood by the computer as 0's and 1's.
  
- **Assembly Language:**
  - Uses symbolic instructions (mnemonics) to represent machine code.
  - More human-readable than machine language.
  - Requires an assembler for translation into machine code.

[Diagram Link](https://prnt.sc/0yoAdPcZFcMK)

## CPU (Central Processing Unit)

- The CPU is at the heart of the computer.
- It fetches, decodes, and executes instructions to produce results.
- Internally, it consists of two parts:
  - Control Unit
  - Arithmetic and Logic Unit (ALU)
- The CPU performs the fetch/decode/execute cycle to process program information.
  - **Fetch:** Retrieve the next instruction.
  - **Decode:** Interpret the instruction.
  - **Execute:** Perform the operation specified by the instruction.

## Main memory (RAM)

- A byte consists of eight bits that may be either on or off.
  - 1 = on
  - 0 = off
- The bits form a pattern that represents a character or a number.
- Each byte in memory is assigned a unique number known as an address.

- For example, a series of bytes with their addresses:
  - The number 149 is stored in the byte at address 16.
  - The number 72 is stored in the byte at address 23.

[Diagram Link](https://prnt.sc/bWuIHPqR1NfY)

## Operating Systems

- An operating system is a set of programs that manages the computer’s hardware devices and controls their processes.
- Most modern operating systems are multitasking and capable of running multiple programs at once.
- Through *scheduling*, an operating system divides the allocation of hardware resources and the attention of the CPU among all the executing programs.

## Application Software

- Application Software
Application software refers to programs that make the computer useful to the user
Application software provides a more specialized type of environment for the user to work in
Common application software:
Spreadsheets
Word processors
Accounting software
Tax software
Games

## Python Language Translation Process
 1. Compiler receives the source code.
 2. Compiler checks each line the syntax.
 3. Compiler finds an error - it displays an error message called a syntax error.
 4. If there is no syntax error, it translates the program to byte code.
 5. Byte code gets sent to Python Virtual Machine.
 6. Byte code checks if there are any imports or inputs and brings them in.
 7. VM executes the byte code. If an error occurs, it displays an runtime error.
 8. Code gets executed and the result is output.

## Python Keywords

- `if`: Used for conditional statements.
- `else`: Used in conjunction with `if` for alternate conditions.
- `elif`: Short for "else if," used for additional conditional checks.
- `while`: Used to create loops with a specified condition.
- `for`: Used for looping over iterable objects.
- `def`: Used to define functions.
- `class`: Used to define classes.
- `return`: Used to return values from functions.
- `import`: Used to import modules or libraries.
- `from`: Used with `import` to specify specific items to import from a module.
- `as`: Used with `import` for aliasing imported modules or items.
- `try`: Begins a block of code for exception handling.
- `except`: Specifies how to handle exceptions in a `try` block.
- `finally`: Specifies code to execute whether an exception occurs or not.
- `raise`: Used to raise exceptions manually.
- `pass`: Placeholder statement, does nothing.
- `break`: Used to exit a loop prematurely.
- `continue`: Skips the rest of the current loop iteration and continues to the next.
- `in`: Used to check if an element is present in an iterable.
- `is`: Used to check if two variables refer to the same object in memory.

## Python Operators

### Arithmetic Operators
- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `%` (Modulus)
- `**` (Exponentiation)
- `//` (Floor Division)

### Comparison Operators
- `==` (Equal)
- `!=` (Not Equal)
- `<` (Less Than)
- `>` (Greater Than)
- `<=` (Less Than or Equal To)
- `>=` (Greater Than or Equal To)

### Assignment Operators
- `=` (Assignment)
- `+=` (Addition Assignment)
- `-=` (Subtraction Assignment)
- `*=` (Multiplication Assignment)
- `/=` (Division Assignment)
- `%=` (Modulus Assignment)
- `**=` (Exponentiation Assignment)
- `//=` (Floor Division Assignment)

### Logical Operators
- `and` (Logical AND)
- `or` (Logical OR)
- `not` (Logical NOT)

### Membership Operators
- `in` (Membership Test)
- `not in` (Negated Membership Test)

### Identity Operators
- `is` (Identity Test)
- `is not` (Negated Identity Test)

## Setting Up Python

- Python 2 vs Python 3
  - Use Python 3
- Go to [python.org](https://www.python.org/) and download and install Python.
- Install it for all users.
- Add it to your system's PATH.
- Open a command window and check the Python version:

## Python Style Guide (PEP 8)
 - PEP (Python Enhancement Proposal) 8 is the standard
 - Lists everything that you need to know about styling Python code
 - A Foolish Consistency is the Hobgoblin of Little Minds
    - “Code is read much more often than it is written” – BDFL 
    - Readability counts (PEP 20)