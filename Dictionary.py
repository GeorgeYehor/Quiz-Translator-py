
operand = None
operator = None
wait_for_number = True

def funk1_operand():
    while wait_for_number:
        try:
            global operand1
            operand1 = float(input('Write a number: '))
            break
        except:
            print('Please, write a number')

def funk2_operand():
    while wait_for_number:
        try:
            global operand2
            operand2 = float(input('Write a number: '))
            break
        except:
            print('Please, write a number')

def funk_operator():
    global operator
    operator = input('Operator: ')
    while operator not in ('+', '-', '*', '/', '='):
        operator = input('Please, write -, +, *, or /: ')

def funk_result1():
    global result
    if operator == '-':
        result = operand1 - operand2
    elif operator == '+':
        result = operand1 + operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2

def funk_result2():
    global result
    if operator == '-':
        result = result - operand
    elif operator == '+':
        result = result + operand
    elif operator == '*':
        result = result * operand
    elif operator == '/':
        result = result / operand


funk1_operand() #operand1 (first float number)
funk_operator() #operator (-, +, *, /)
funk2_operand() #operand2 (second float number)
funk_result1()  #result   (operand1 operator operand2)

while operator != '=':
    funk_operator()  # operator (-, +, *, /)
    if operator == '=':
        break
    while wait_for_number:
        try:
            operand = float(input('Write a number: '))
            break
        except:
            print('Please, write a number')
    funk_result2() #result   (result operator operand)




print(result)










