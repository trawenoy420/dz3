import sys

result = 0
while True:
    line = input("Введите число или 'q' для выхода: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f"Сумма - {result}. Конец")
                exit(0)
            else:
                print(f"Сумма - {result}", file=sys.stderr)
                exit(1)
print(result)
exit()