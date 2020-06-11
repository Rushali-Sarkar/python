PLUS = "+"
MINUS = "-"
DOLLAR = "$"
SPACE = " "

def remove_extra_characters(expression: str) -> str:
    return expression.replace(SPACE, "").replace(PLUS, SPACE + PLUS).replace(MINUS, SPACE + MINUS).strip(DOLLAR).strip(SPACE).strip(PLUS)

def add_extra_characters(expression: str) -> str:
    return DOLLAR + expression.replace(PLUS, SPACE + PLUS).replace(MINUS, SPACE + MINUS + SPACE) + DOLLAR

def add_remove_plus(expression: str) -> str:
    if expression.startswith(PLUS):
        return expression[1: ]
    if not expression.startswith(MINUS):
        return PLUS + expression
    return expression

def usual_to_mathematician(expression: str) -> str:
    expression = add_remove_plus(remove_extra_characters(expression))
    expression = "".join(reversed(expression.split(SPACE)))
    return add_extra_characters((add_remove_plus(expression)))

print(usual_to_mathematician("$ + 3x^4+4x^3-5x^2+4x-19$"))
        
    
    


























    
















