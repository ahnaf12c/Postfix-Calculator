# Postfix Expression Calculator

## Description
This project is a calculator that evaluates postfix expressions (also known as Reverse Polish Notation). It allows users to input mathematical expressions using numbers and operators, evaluates the expression using a stack-based algorithm, and outputs the result. The calculator can handle both integer and floating-point numbers and provides basic error handling for invalid expressions and operations.
To learn more about Postfix and other notations, see:
- https://en.wikipedia.org/wiki/Reverse_Polish_notation
- https://en.wikipedia.org/wiki/Polish_notation
- https://en.wikipedia.org/wiki/Infix_notation

## Features
- **Postfix Expression Evaluation**: Supports basic arithmetic operations: addition, subtraction, multiplication, division, and exponentiation.
- **Error Handling**: Detects syntax errors, division by zero, and invalid characters.
- **User Commands**:
  - `'q'`: Exit the calculator
  - `'clr'`: Clear the current answer
  - `'ans`: Show the current answer
  - `'h'`: Display help instructions
- **Operations**:
  - `+`: Addition
  - `-`: Substraction
  - `*`: Multiplication
  - `/`: Division
  - `^`: Exponentiation
  - `&`, `|` and `v`: Bitwise `AND`, `OR` and `XOR` respectively 
- **Any syntax error now automatically clears the stack**

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
2. Ensure you have Python 3.x installed
3. Run the executable in the 'dist' folder

## Usage
1. Start the program, and you will be prompted to enter a postfix expression.
2. Enter your expression (e.g., 3 4 +).
3. The result will be displayed, or an error message will be shown if the expression is invalid.
4. Use the commands for additional functionality.

## Example
1. ```plaintext
   Please enter a postfix expression ('q' to exit, 'h' for help): 3 4 +
   Result: 7.0

## Version
 - Version: Release 1.0.1
 - Features of 1.0.1:
   - Added logical operations (bitwise `OR`, `AND` and `XOR`)
   - Improved error handling a bit
   - Added one new command (`ans` command)

## Support
For any questions or issues, please create an issue in the GitHub repository or contact me via ahnaf101109@gmail.com

## Acknowledgments
- This project was inspired by my interest in the Postfix notation and the overall workings of a calculator.
- Special thanks to the online programming community and the internet for their valuable resources and support.

## License
This project is licensed under the GNU GPL v3.0 License - see the LICENSE file for details.
