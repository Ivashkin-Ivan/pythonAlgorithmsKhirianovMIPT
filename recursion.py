def matryoshka(n):
    if n == 1:
        print('Матрёшечка')
    else:
        print("Верх матрёшки n=", n)
        matryoshka(n-1)
        print("Низ матрёшки n=", n)
def gcd(a,b):
    return(a if b == 0 else gcd(b,a % b))

def faktorial(n:int):
    if n <= 0:
        return 1
    return faktorial(n-1) * n
def pow(a:int, n:int):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a,n-1) * a
    else: return pow(a ** 2,n // 2)
'''def khanoy_tower'''
def generate_numbers(N:int, M:int, prefix = None):
    '''Генерирует все числа (с лидирующими) в N-ричной системе счисления (N<=10) длины M'''
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N,M-1,prefix)
        prefix.pop()
def generate_permetations(N:int,M:int =-1,prefix=None):
    '''Генерирует всех перестановок N чисел в M позициях, с префиксом prefix'''
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permetations(N, M-1, prefix)
        prefix.pop()
def find(number,A):
    '''Ищет x в A и возвращает True, если такой есть, False, если такого нет'''
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag
print(faktorial(4))
print(gcd(21,91))
print(matryoshka(5))
print(pow(3,2))
'''print(generate_numbers(25,3))'''
print(generate_permetations(3)) # для реализации используем внутреннюю функцию find
