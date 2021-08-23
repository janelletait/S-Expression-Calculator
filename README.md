# S-Expression-Calculator

This calculator simplifies and evaluates s-expressions via standard input.

Supported functions: addition and multiplication

Syntax: (FUNCTION EXPR EXPR) where FUNCTION is either "add" or "multiply" and EXPR can be any integer or further function call.

Sample input and output:


INPUT: 123\
OUTPUT: 123

INPUT: (add 3 4)\
OUTPUT: 7

INPUT: (multiply 3 4)\
OUTPUT: 12

INPUT: (multiply 3 (add 1 2))\
OUTPUT: 9
