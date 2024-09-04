class FormulaError(Exception):
    pass

def calculate(formula):
    try:
        num1, operator, num2 = formula.split()
    except ValueError:
        raise FormulaError("Invalid formula.")

    if len(formula.split()) != 3:
        raise FormulaError("Invalid formula.")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise FormulaError("Invalid number format.")

    if operator != "+" and operator != "-":
        raise FormulaError("Invalid operator.")

    if operator == "+":
        result = num1 + num2
    else:
        result = num1 - num2

    return result

while True:
    formula = input("Enter a formula (number +/- number) or enter 'quit' to exit: ")
    if formula == "quit":
        break
    else:
        print(calculate(formula))