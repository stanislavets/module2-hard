n = int(input( "Введите число от 3 до 20: "))
result = ''
for a in range(1, n):
    for b in range(a + 1, n):
        if n % (a + b) == 0:
            result = result + f'{a}{b}'
print(result, end="")



