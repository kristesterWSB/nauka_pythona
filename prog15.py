import sys
def calculator(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    else:
        print('Wybierz + - * / ')
    raise AssertionError('buuum')



if __name__ == '__main__':
    suma = calculator(1,2,'+')
    print(suma)
    roznica = calculator(2,2,'-')
    print(roznica)
    iloczyn = calculator(2,3,'*')
    print(iloczyn)
    iloraz = calculator(6,2,'/')
    print(iloraz)
    inne = calculator(6,6,'a')
    print(inne)
