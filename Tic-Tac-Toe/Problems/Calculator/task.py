# put your python code here
a = float(input())
b = float(input())
c = input()
if c in ('/', 'mod', 'div') and b == 0:
    print("Division by 0!")
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
elif c == 'mod':
    print(a % b)
elif c == 'div':
    print(a // b)
elif c == 'pow':
    print(a ** b)