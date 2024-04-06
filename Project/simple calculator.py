while True:
    number1 = float(input("Enter a number: "))
    op = input("Enter a operator: ")
    number2 = float(input("Enter another number: "))

    result = 0

    if op == '+':
        result = number1 + number2 
    elif op == '-':
        result = number1 - number2
    elif op == '*':
        result = number1 * number2
    elif op == '/':
        result = number1 / number2
    elif op == '%':
        result = number1 % number2
    else:
        result = "Enter a valid operator"
    print(f'{number1} {op} {number2} = {result}')

    d = input("Do you want to continue? if yes enter Y else N: ")
    if d == 'Y' or d == 'y':
        continue
    else:
        break  
    
