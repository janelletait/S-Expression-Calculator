"""
----------------------------------------------
Author: Janelle Tait
Email: taitjane110@gmail.com
----------------------------------------------
"""

class S_Expression:

    def calculate(self, input_str):
        
        #Proceed so long as the current s-expression is not empty (if it is, either an error occurred or the user entered a blank line so the program must stop).
        while len(input_str) >= 1:
            
            #If the expression is just an integer, simply return it.
            if input_str.isnumeric() == True:
                return int(input_str)
 
            closing_bracket_index = 0
            opening_bracket_index = 0
            
            #Following BEDMAS, start with the expression in the most inner brackets.
            #The first closing bracket in the input string marks the ending of the most inner expression. 
            for i in range(0, len(input_str)):
                if input_str[i] == ')':
                    closing_bracket_index = i
                    break

            #The opening bracket of the most inner expression is the closest one to the left of its closing bracket.
            for j in range(closing_bracket_index-1, 0, -1):
                if input_str[j] == '(':
                    opening_bracket_index = j
                    break

            #The most inner expression can now be evaluated since it must not have nested expressions inside.
            value = self.evaluate_expression(input_str[opening_bracket_index + 1 : closing_bracket_index])
            
            #If the opening bracket of the evaluated expression was at the first index of the input string, it was the most outer expression so the final result has been found.
            if opening_bracket_index == 0:
                return value

            #Simplify the input string by replacing the evaluated expression with its calculated value.
            else:
                input_str = input_str[ : opening_bracket_index] + str(value) + input_str[closing_bracket_index + 1 : ]               

        return int(input_str)

    #This function evaluates simple expressions that have no nested functions.
    def evaluate_expression(self, input_expr):

        #Split the input expression into 3 parts: the name of the function to be performed, and the two numbers involved.
        function_elements = input_expr.split()

        if function_elements[0] == 'multiply':
            result = int(function_elements[1]) * int(function_elements[2])

        elif function_elements[0] == 'add':
            result = int(function_elements[1]) + int(function_elements[2])

        else:
            result = int(input_expr)

        return result


def main():
    usr_input = input()
    print(S_Expression().calculate(usr_input))


if __name__ == '__main__':
    main()