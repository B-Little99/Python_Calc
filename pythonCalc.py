def addition(a, b):
    a = int(a)
    b = int(b)
    result = a + b
    print(result)

def subtraction(a, b):
    a = int(a)
    b = int(b)
    result = a - b
    print(result)

def multiplication(a, b):
    a = int(a)
    b = int(b)
    result = a * b
    print(result)

def division(a, b):
    a = int(a)
    b = int(b)
    result = a / b
    print(result)

print('\n \nWelcome to SimpleCalc! \n \nThis is a simplistic calculator. We only handle addition, multiplication, subtraction and division of two numbers only.')

loop = True

while loop == True:

    print('Please enter your calculation or enter "done" if you wish to exit: ')

    calculation = input()

    if calculation == 'done':
        print('Thanks for using SimpleCalc! Have a good day.')
        loop = False
    else: 
        calculationList = calculation.split()

        num1 = calculationList[0]
        calcSymbol = calculationList[1]
        num2 = calculationList[2]
    
        if calcSymbol == '+':
            addition(num1, num2)
        elif calcSymbol == '-':
            subtraction(num1, num2)
        elif calcSymbol == '*':
            multiplication(num1, num2)
        else:
            division(num1, num2)