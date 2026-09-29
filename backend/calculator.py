def calculator(expression):
    operands = []
    operators = []
    current_number = ""
    after_number = False
    for i, char in enumerate(expression):
        j = i - 1
        while j>=0 and expression[j] == " ":
            j -= 1
        if char.isdigit() or char == "." or (char == '-' and(j == -1 or expression[j] in ('+', '-', '*', "/", "%"))):
            if after_number is True:
                return "Invalid Expression"
            else:
                current_number += char
        elif char == " ":
            if current_number!= "":
                after_number = True
            else:
                after_number = False
        else:
            if current_number == "" or current_number.count('.')>1 or not any(character.isdigit() for character in current_number):
                return "Invalid Expression"
            else:
                operands.append(float(current_number))
                operators.append(char)
                current_number = ""
                after_number = False
    if current_number == "" or current_number.count('.')>1 or not any(character.isdigit() for character in current_number):
        return "Invalid Expression"
    else:
        operands.append(float(current_number))
    return operands, operators
def evaluate(operands, operators):
    precedence = {'+' : 1, '-': 1, '*': 2, "/": 2, "%" : 2}
    while operators:
        highest_precedence = 0
        highest_operator = "+"
        operator_index = 0
        for i, token in enumerate(operators):
            if precedence[token] > highest_precedence:
                highest_precedence = precedence[token]
                highest_operator = token
                operator_index = i
        left_operand = operands[operator_index]
        right_operand = operands[operator_index + 1]
        if highest_operator == '+':
            result = left_operand + right_operand
        elif highest_operator == '-':
            result = left_operand - right_operand
        elif highest_operator == '*':
            result = left_operand * right_operand
        elif highest_operator == '/':
            if right_operand == 0:
                return "cannot divide by zero"
            else:
                result = left_operand / right_operand
        elif highest_operator == "%":
            if right_operand == 0:
                return "cannot divide by zero"
            else:
                result = left_operand % right_operand
        operands[operator_index] = result
        del operators[operator_index]
        del operands[operator_index + 1]
    if operators == []:
        return operands[0]
def calculator_expression(expression):
    parsed = calculator(expression)
    if parsed == "Invalid Expression":
        return parsed
    else:
        operands, operators = parsed
        result = evaluate(operands, operators)
        return result
    
if __name__ == "__main__":
    expression = input("Expression")
    parsed = calculator(expression)
    if parsed == 'Invalid Expression':
        print(parsed)
    else:
        operands, operators = parsed
        result = evaluate(operands, operators)
        print(result)



