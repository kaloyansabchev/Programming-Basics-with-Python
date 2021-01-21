n1 = int(input())
n2 = int(input())
operatora = input()

result = 0
result_type = ''

if n2 == 0 and operatora == '/' or n2 == 0 and operatora == '%':
    print(f"Cannot divide {n1} by zero")
    quit()

if operatora == '+':
    result = n1 + n2
elif operatora == '-':
    result = n1 - n2
elif operatora == '*':
    result = n1 * n2
elif operatora == '/':
    result = n1 / n2
elif operatora == '%':
    result = n1 % n2

if result % 2 == 0:
    result_type = 'even'
else:
    result_type = 'odd'

if operatora == '+' or operatora == '-' or operatora == '*':
    print(f'{n1} {operatora} {n2} = {result} - {result_type}')
elif operatora == '/':
    print(f'{n1} / {n2} = {result:.2f}')
elif operatora == '%':
    print(f'{n1} % {n2} = {result}')