# S-Expression-Calculator

This calculator simplifies and evaluates s-expressions from the command line.

Supported functions: addition and multiplication

Syntax: (FUNCTION EXPR EXPR) where FUNCTION is either "add" or "multiply" and EXPR can be any integer or further function call.

Sample input and output:

python calc.py "123"

123

python calc.py "(add 3 4)"

7

python calc.py "(multiply 3 4)"

12

python calc.py "(multiply 3 (add 1 2))"

9
